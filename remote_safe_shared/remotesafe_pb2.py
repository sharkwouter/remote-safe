# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remotesafe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='remotesafe.proto',
  package='remotesafe',
  syntax='proto3',
  serialized_pb=_b('\n\x10remotesafe.proto\x12\nremotesafe\"2\n\x04\x46ile\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06sha256\x18\x02 \x01(\t\x12\x0c\n\x04\x66ile\x18\x03 \x01(\x0c\"\x18\n\x08\x46ileInfo\x12\x0c\n\x04path\x18\x01 \x01(\t\"/\n\x08\x46ileList\x12#\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x14.remotesafe.FileInfo\"\x07\n\x05\x45mpty2|\n\x0bsyncHandler\x12\x33\n\x07GetFile\x12\x14.remotesafe.FileInfo\x1a\x10.remotesafe.File\"\x00\x12\x38\n\x0bGetFileList\x12\x11.remotesafe.Empty\x1a\x14.remotesafe.FileList\"\x00\x62\x06proto3')
)




_FILE = _descriptor.Descriptor(
  name='File',
  full_name='remotesafe.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='remotesafe.File.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha256', full_name='remotesafe.File.sha256', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='remotesafe.File.file', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=82,
)


_FILEINFO = _descriptor.Descriptor(
  name='FileInfo',
  full_name='remotesafe.FileInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='remotesafe.FileInfo.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=108,
)


_FILELIST = _descriptor.Descriptor(
  name='FileList',
  full_name='remotesafe.FileList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='remotesafe.FileList.files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=157,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='remotesafe.Empty',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=166,
)

_FILELIST.fields_by_name['files'].message_type = _FILEINFO
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['FileInfo'] = _FILEINFO
DESCRIPTOR.message_types_by_name['FileList'] = _FILELIST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'remotesafe_pb2'
  # @@protoc_insertion_point(class_scope:remotesafe.File)
  ))
_sym_db.RegisterMessage(File)

FileInfo = _reflection.GeneratedProtocolMessageType('FileInfo', (_message.Message,), dict(
  DESCRIPTOR = _FILEINFO,
  __module__ = 'remotesafe_pb2'
  # @@protoc_insertion_point(class_scope:remotesafe.FileInfo)
  ))
_sym_db.RegisterMessage(FileInfo)

FileList = _reflection.GeneratedProtocolMessageType('FileList', (_message.Message,), dict(
  DESCRIPTOR = _FILELIST,
  __module__ = 'remotesafe_pb2'
  # @@protoc_insertion_point(class_scope:remotesafe.FileList)
  ))
_sym_db.RegisterMessage(FileList)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'remotesafe_pb2'
  # @@protoc_insertion_point(class_scope:remotesafe.Empty)
  ))
_sym_db.RegisterMessage(Empty)



_SYNCHANDLER = _descriptor.ServiceDescriptor(
  name='syncHandler',
  full_name='remotesafe.syncHandler',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=168,
  serialized_end=292,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFile',
    full_name='remotesafe.syncHandler.GetFile',
    index=0,
    containing_service=None,
    input_type=_FILEINFO,
    output_type=_FILE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFileList',
    full_name='remotesafe.syncHandler.GetFileList',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_FILELIST,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYNCHANDLER)

DESCRIPTOR.services_by_name['syncHandler'] = _SYNCHANDLER

# @@protoc_insertion_point(module_scope)
