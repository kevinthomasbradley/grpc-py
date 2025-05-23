# grpc-py
gRPC Python Microservices

## Setup
> python3 -m venv venv
> source venv/bin/activate
> pip3 install grpcio
> pip3 install grpcio-tools

> python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto