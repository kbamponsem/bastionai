use private_learning::{l2_loss, Optimizer, SGD};
use std::collections::HashMap;
use std::sync::RwLock;
use tch::vision::dataset;
use tch::Tensor;
use tokio::sync::mpsc;
use tokio_stream::wrappers::ReceiverStream;
use tonic::{transport::Server, Request, Response, Status, Streaming};
use uuid::Uuid;

mod remote_torch {
    tonic::include_proto!("remote_torch");
}
use remote_torch::remote_torch_server::{RemoteTorch, RemoteTorchServer};
use remote_torch::{
    Accuracy, Chunk, Empty, Reference, References, TestConfig, TrainConfig, TrainingProgress,
};

mod storage;
use storage::{Artifact, Dataset, Module};

mod utils;
use utils::*;

struct BastionAIServer {
    modules: RwLock<HashMap<Uuid, Artifact<Module>>>,
    datasets: RwLock<HashMap<Uuid, Artifact<Dataset>>>,
}

impl BastionAIServer {
    pub fn new() -> Self {
        BastionAIServer {
            modules: RwLock::new(HashMap::new()),
            datasets: RwLock::new(HashMap::new()),
        }
    }
}

#[tonic::async_trait]
impl RemoteTorch for BastionAIServer {
    type FetchDatasetStream = ReceiverStream<Result<Chunk, Status>>;
    type FetchModuleStream = ReceiverStream<Result<Chunk, Status>>;
    type TrainStream = ReceiverStream<Result<TrainingProgress, Status>>;

    async fn send_dataset(
        &self,
        request: Request<Streaming<Chunk>>,
    ) -> Result<Response<Reference>, Status> {
        let dataset: Artifact<Dataset> =
            tcherror_to_status((unstream_data(request.into_inner()).await?).deserialize())?;
        let description = String::from(dataset.description.clone());
        let identifier = Uuid::new_v4();

        self.datasets
            .write()
            .unwrap()
            .insert(identifier.clone(), dataset);

        Ok(Response::new(Reference {
            identifier: format!("{}", identifier),
            description,
        }))
    }

    async fn send_model(
        &self,
        request: Request<Streaming<Chunk>>,
    ) -> Result<Response<Reference>, Status> {
        let module: Artifact<Module> =
            tcherror_to_status(unstream_data(request.into_inner()).await?.deserialize())?;
        let description = String::from(module.description.clone());
        let identifier = Uuid::new_v4();

        self.modules
            .write()
            .unwrap()
            .insert(identifier.clone(), module);
        Ok(Response::new(Reference {
            identifier: format!("{}", identifier),
            description,
        }))
    }

    async fn fetch_dataset(
        &self,
        request: Request<Reference>,
    ) -> Result<Response<Self::FetchDatasetStream>, Status> {
        let identifier = parse_reference(request.into_inner())?;
        let serialized = {
            let datasets = self.datasets.read().unwrap();
            let artifact = datasets
                .get(&identifier)
                .ok_or(Status::not_found("Not found"))?;
            tcherror_to_status(artifact.serialize())?
        };

        Ok(stream_data(serialized, 100_000_000).await)
    }

    async fn fetch_module(
        &self,
        request: Request<Reference>,
    ) -> Result<Response<Self::FetchModuleStream>, Status> {
        let identifier = parse_reference(request.into_inner())?;
        let serialized = {
            let modules = self.modules.read().unwrap();
            let artifact = modules
                .get(&identifier)
                .ok_or(Status::not_found("Not found"))?;
            tcherror_to_status(artifact.serialize())?
        };

        Ok(stream_data(serialized, 100_000_000).await)
    }

    async fn delete_dataset(&self, request: Request<Reference>) -> Result<Response<Empty>, Status> {
        let identifier = parse_reference(request.into_inner())?;
        self.datasets.write().unwrap().remove(&identifier);
        Ok(Response::new(Empty {}))
    }

    async fn delete_module(&self, request: Request<Reference>) -> Result<Response<Empty>, Status> {
        let identifier = parse_reference(request.into_inner())?;
        self.modules.write().unwrap().remove(&identifier);
        Ok(Response::new(Empty {}))
    }

    async fn train(
        &self,
        request: Request<TrainConfig>,
    ) -> Result<Response<Self::TrainStream>, Status> {
        let config = request.into_inner();
        let dataset_id = parse_reference(
            config
                .dataset
                .clone()
                .ok_or(Status::invalid_argument("Not found"))?,
        )?;
        let module_id = parse_reference(
            config
                .model
                .clone()
                .ok_or(Status::invalid_argument("Not found"))?,
        )?;
        let (mut tx, rx) = mpsc::channel(5);
        {
            let datasets = self.datasets.read().unwrap();
            let modules = self.modules.read().unwrap();
            let dataset = datasets
                .get(&dataset_id)
                .ok_or(Status::not_found("Not found"))?;
            let module = modules
                .get(&module_id)
                .ok_or(Status::not_found("Not found"))?;

            let trainer = tcherror_to_status(module.data.train(&dataset.data, config))?;
            let trainer = Box::leak(trainer);
            tokio::spawn(async move {
                for it in trainer.iter() {
                    let (epoch, pos, loss) = it;
                }
                tx.send(Ok(TrainingProgress::default())).await.unwrap();
            });
        }
        // unimplemented!()
        Ok(Response::new(ReceiverStream::new(rx)))
    }

    async fn test(&self, request: Request<TestConfig>) -> Result<Response<Accuracy>, Status> {
        let config = request.into_inner();
        let dataset_id = parse_reference(
            config
                .dataset
                .clone()
                .ok_or(Status::invalid_argument("Not found"))?,
        )?;
        let module_id = parse_reference(
            config
                .model
                .clone()
                .ok_or(Status::invalid_argument("Not found"))?,
        )?;
        let accuracy = {
            let datasets = self.datasets.read().unwrap();
            let modules = self.modules.read().unwrap();
            let dataset = datasets
                .get(&dataset_id)
                .ok_or(Status::not_found("Not found"))?;
            let module = modules
                .get(&module_id)
                .ok_or(Status::not_found("Not found"))?;
            tcherror_to_status(module.data.test(&dataset.data, config))?
        };
        Ok(Response::new(Accuracy { value: accuracy }))
    }

    async fn available_models(
        &self,
        _request: Request<Empty>,
    ) -> Result<Response<References>, Status> {
        let list = self
            .modules
            .read()
            .unwrap()
            .iter()
            .map(|(k, v)| Reference {
                identifier: format!("{}", k),
                description: v.description.clone(),
            })
            .collect();

        Ok(Response::new(References { list }))
    }

    async fn available_datasets(
        &self,
        _request: Request<Empty>,
    ) -> Result<Response<References>, Status> {
        let list = self
            .datasets
            .read()
            .unwrap()
            .iter()
            .map(|(k, v)| Reference {
                identifier: format!("{}", k),
                description: v.description.clone(),
            })
            .collect();

        Ok(Response::new(References { list }))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse()?;
    let server = BastionAIServer::new();

    println!("BastionAI listening on {:?}", addr);
    Server::builder()
        .add_service(RemoteTorchServer::new(server))
        .serve(addr)
        .await?;

    Ok(())
}
