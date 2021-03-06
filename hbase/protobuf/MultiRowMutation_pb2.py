# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MultiRowMutation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Client_pb2 as Client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='MultiRowMutation.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16MultiRowMutation.proto\x1a\x0c\x43lient.proto\"\"\n MultiRowMutationProcessorRequest\"#\n!MultiRowMutationProcessorResponse\"a\n\x11MutateRowsRequest\x12(\n\x10mutation_request\x18\x01 \x03(\x0b\x32\x0e.MutationProto\x12\x13\n\x0bnonce_group\x18\x02 \x01(\x04\x12\r\n\x05nonce\x18\x03 \x01(\x04\"\x14\n\x12MutateRowsResponse2P\n\x17MultiRowMutationService\x12\x35\n\nMutateRows\x12\x12.MutateRowsRequest\x1a\x13.MutateRowsResponseBL\n*org.apache.hadoop.hbase.protobuf.generatedB\x16MultiRowMutationProtosH\x01\x88\x01\x01\xa0\x01\x01')
  ,
  dependencies=[Client__pb2.DESCRIPTOR,])




_MULTIROWMUTATIONPROCESSORREQUEST = _descriptor.Descriptor(
  name='MultiRowMutationProcessorRequest',
  full_name='MultiRowMutationProcessorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=74,
)


_MULTIROWMUTATIONPROCESSORRESPONSE = _descriptor.Descriptor(
  name='MultiRowMutationProcessorResponse',
  full_name='MultiRowMutationProcessorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=111,
)


_MUTATEROWSREQUEST = _descriptor.Descriptor(
  name='MutateRowsRequest',
  full_name='MutateRowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mutation_request', full_name='MutateRowsRequest.mutation_request', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce_group', full_name='MutateRowsRequest.nonce_group', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='MutateRowsRequest.nonce', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=210,
)


_MUTATEROWSRESPONSE = _descriptor.Descriptor(
  name='MutateRowsResponse',
  full_name='MutateRowsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=232,
)

_MUTATEROWSREQUEST.fields_by_name['mutation_request'].message_type = Client__pb2._MUTATIONPROTO
DESCRIPTOR.message_types_by_name['MultiRowMutationProcessorRequest'] = _MULTIROWMUTATIONPROCESSORREQUEST
DESCRIPTOR.message_types_by_name['MultiRowMutationProcessorResponse'] = _MULTIROWMUTATIONPROCESSORRESPONSE
DESCRIPTOR.message_types_by_name['MutateRowsRequest'] = _MUTATEROWSREQUEST
DESCRIPTOR.message_types_by_name['MutateRowsResponse'] = _MUTATEROWSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MultiRowMutationProcessorRequest = _reflection.GeneratedProtocolMessageType('MultiRowMutationProcessorRequest', (_message.Message,), dict(
  DESCRIPTOR = _MULTIROWMUTATIONPROCESSORREQUEST,
  __module__ = 'MultiRowMutation_pb2'
  # @@protoc_insertion_point(class_scope:MultiRowMutationProcessorRequest)
  ))
_sym_db.RegisterMessage(MultiRowMutationProcessorRequest)

MultiRowMutationProcessorResponse = _reflection.GeneratedProtocolMessageType('MultiRowMutationProcessorResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTIROWMUTATIONPROCESSORRESPONSE,
  __module__ = 'MultiRowMutation_pb2'
  # @@protoc_insertion_point(class_scope:MultiRowMutationProcessorResponse)
  ))
_sym_db.RegisterMessage(MultiRowMutationProcessorResponse)

MutateRowsRequest = _reflection.GeneratedProtocolMessageType('MutateRowsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEROWSREQUEST,
  __module__ = 'MultiRowMutation_pb2'
  # @@protoc_insertion_point(class_scope:MutateRowsRequest)
  ))
_sym_db.RegisterMessage(MutateRowsRequest)

MutateRowsResponse = _reflection.GeneratedProtocolMessageType('MutateRowsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEROWSRESPONSE,
  __module__ = 'MultiRowMutation_pb2'
  # @@protoc_insertion_point(class_scope:MutateRowsResponse)
  ))
_sym_db.RegisterMessage(MutateRowsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\026MultiRowMutationProtosH\001\210\001\001\240\001\001'))

_MULTIROWMUTATIONSERVICE = _descriptor.ServiceDescriptor(
  name='MultiRowMutationService',
  full_name='MultiRowMutationService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=234,
  serialized_end=314,
  methods=[
  _descriptor.MethodDescriptor(
    name='MutateRows',
    full_name='MultiRowMutationService.MutateRows',
    index=0,
    containing_service=None,
    input_type=_MUTATEROWSREQUEST,
    output_type=_MUTATEROWSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MULTIROWMUTATIONSERVICE)

DESCRIPTOR.services_by_name['MultiRowMutationService'] = _MULTIROWMUTATIONSERVICE

# @@protoc_insertion_point(module_scope)
