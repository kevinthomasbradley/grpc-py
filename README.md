# grpc-py
gRPC Python Microservices

## Setup
1. python3 -m venv venv
2. source venv/bin/activate
3. pip3 install grpcio
4. pip3 install grpcio-tools

> python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto