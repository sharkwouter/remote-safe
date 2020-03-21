default: build-proto

build-proto:
	python3 -m grpc_tools.protoc -I protos --python_out=remote_safe_shared --grpc_python_out=remote_safe_shared protos/remotesafe.proto
