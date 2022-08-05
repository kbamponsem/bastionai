# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_torch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12remote_torch.proto\x12\x0cremote_torch\"4\n\tReference\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\":\n\x05\x43hunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06secret\x18\x03 \x01(\x0c\"\x07\n\x05\x45mpty\"\xb4\x01\n\x0bTrainConfig\x12&\n\x05model\x18\x01 \x01(\x0b\x32\x17.remote_torch.Reference\x12(\n\x07\x64\x61taset\x18\x02 \x01(\x0b\x32\x17.remote_torch.Reference\x12\x18\n\x10private_learning\x18\x03 \x01(\x08\x12\x12\n\nbatch_size\x18\x04 \x01(\x05\x12\x0e\n\x06\x65pochs\x18\x05 \x01(\x05\x12\x15\n\rlearning_rate\x18\x06 \x01(\x02\"r\n\nTestConfig\x12&\n\x05model\x18\x01 \x01(\x0b\x32\x17.remote_torch.Reference\x12(\n\x07\x64\x61taset\x18\x02 \x01(\x0b\x32\x17.remote_torch.Reference\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\"3\n\nReferences\x12%\n\x04list\x18\x01 \x03(\x0b\x32\x17.remote_torch.Reference\"\x19\n\x08\x41\x63\x63uracy\x12\r\n\x05value\x18\x01 \x01(\x02\"A\n\x10TrainingProgress\x12\r\n\x05\x65poch\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x05\x12\x0c\n\x04loss\x18\x03 \x01(\x0c\x32\x9f\x05\n\x0bRemoteTorch\x12?\n\x0bSendDataset\x12\x13.remote_torch.Chunk\x1a\x17.remote_torch.Reference\"\x00(\x01\x12=\n\tSendModel\x12\x13.remote_torch.Chunk\x1a\x17.remote_torch.Reference\"\x00(\x01\x12@\n\x0c\x46\x65tchDataset\x12\x17.remote_torch.Reference\x1a\x13.remote_torch.Chunk\"\x00\x30\x01\x12?\n\x0b\x46\x65tchModule\x12\x17.remote_torch.Reference\x1a\x13.remote_torch.Chunk\"\x00\x30\x01\x12?\n\rDeleteDataset\x12\x17.remote_torch.Reference\x1a\x13.remote_torch.Empty\"\x00\x12>\n\x0c\x44\x65leteModule\x12\x17.remote_torch.Reference\x1a\x13.remote_torch.Empty\"\x00\x12\x42\n\x0f\x41vailableModels\x12\x13.remote_torch.Empty\x1a\x18.remote_torch.References\"\x00\x12\x44\n\x11\x41vailableDatasets\x12\x13.remote_torch.Empty\x1a\x18.remote_torch.References\"\x00\x12\x46\n\x05Train\x12\x19.remote_torch.TrainConfig\x1a\x1e.remote_torch.TrainingProgress\"\x00\x30\x01\x12:\n\x04Test\x12\x18.remote_torch.TestConfig\x1a\x16.remote_torch.Accuracy\"\x00\x62\x06proto3')



_REFERENCE = DESCRIPTOR.message_types_by_name['Reference']
_CHUNK = DESCRIPTOR.message_types_by_name['Chunk']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_TRAINCONFIG = DESCRIPTOR.message_types_by_name['TrainConfig']
_TESTCONFIG = DESCRIPTOR.message_types_by_name['TestConfig']
_REFERENCES = DESCRIPTOR.message_types_by_name['References']
_ACCURACY = DESCRIPTOR.message_types_by_name['Accuracy']
_TRAININGPROGRESS = DESCRIPTOR.message_types_by_name['TrainingProgress']
Reference = _reflection.GeneratedProtocolMessageType('Reference', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCE,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.Reference)
  })
_sym_db.RegisterMessage(Reference)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.Chunk)
  })
_sym_db.RegisterMessage(Chunk)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.Empty)
  })
_sym_db.RegisterMessage(Empty)

TrainConfig = _reflection.GeneratedProtocolMessageType('TrainConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRAINCONFIG,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.TrainConfig)
  })
_sym_db.RegisterMessage(TrainConfig)

TestConfig = _reflection.GeneratedProtocolMessageType('TestConfig', (_message.Message,), {
  'DESCRIPTOR' : _TESTCONFIG,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.TestConfig)
  })
_sym_db.RegisterMessage(TestConfig)

References = _reflection.GeneratedProtocolMessageType('References', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCES,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.References)
  })
_sym_db.RegisterMessage(References)

Accuracy = _reflection.GeneratedProtocolMessageType('Accuracy', (_message.Message,), {
  'DESCRIPTOR' : _ACCURACY,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.Accuracy)
  })
_sym_db.RegisterMessage(Accuracy)

TrainingProgress = _reflection.GeneratedProtocolMessageType('TrainingProgress', (_message.Message,), {
  'DESCRIPTOR' : _TRAININGPROGRESS,
  '__module__' : 'remote_torch_pb2'
  # @@protoc_insertion_point(class_scope:remote_torch.TrainingProgress)
  })
_sym_db.RegisterMessage(TrainingProgress)

_REMOTETORCH = DESCRIPTOR.services_by_name['RemoteTorch']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REFERENCE._serialized_start=36
  _REFERENCE._serialized_end=88
  _CHUNK._serialized_start=90
  _CHUNK._serialized_end=148
  _EMPTY._serialized_start=150
  _EMPTY._serialized_end=157
  _TRAINCONFIG._serialized_start=160
  _TRAINCONFIG._serialized_end=340
  _TESTCONFIG._serialized_start=342
  _TESTCONFIG._serialized_end=456
  _REFERENCES._serialized_start=458
  _REFERENCES._serialized_end=509
  _ACCURACY._serialized_start=511
  _ACCURACY._serialized_end=536
  _TRAININGPROGRESS._serialized_start=538
  _TRAININGPROGRESS._serialized_end=603
  _REMOTETORCH._serialized_start=606
  _REMOTETORCH._serialized_end=1277
# @@protoc_insertion_point(module_scope)
