# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/sleep.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/sleep.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12protos/sleep.proto\"\x18\n\x07Seconds\x12\r\n\x05value\x18\x01 \x01(\x05\x32*\n\tSleepTime\x12\x1d\n\x05Sleep\x12\x08.Seconds\x1a\x08.Seconds\"\x00\x62\x06proto3'
)




_SECONDS = _descriptor.Descriptor(
  name='Seconds',
  full_name='Seconds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Seconds.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=46,
)

DESCRIPTOR.message_types_by_name['Seconds'] = _SECONDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Seconds = _reflection.GeneratedProtocolMessageType('Seconds', (_message.Message,), {
  'DESCRIPTOR' : _SECONDS,
  '__module__' : 'protos.sleep_pb2'
  # @@protoc_insertion_point(class_scope:Seconds)
  })
_sym_db.RegisterMessage(Seconds)



_SLEEPTIME = _descriptor.ServiceDescriptor(
  name='SleepTime',
  full_name='SleepTime',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=48,
  serialized_end=90,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sleep',
    full_name='SleepTime.Sleep',
    index=0,
    containing_service=None,
    input_type=_SECONDS,
    output_type=_SECONDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SLEEPTIME)

DESCRIPTOR.services_by_name['SleepTime'] = _SLEEPTIME

# @@protoc_insertion_point(module_scope)
