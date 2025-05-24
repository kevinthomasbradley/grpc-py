# grpc-py

A Python gRPC Client and Server implementation demonstrating four types of RPC calls.

## Overview

This project showcases the following gRPC call types:

### 1. Unary
- **Description**: The client sends a single request and receives a single response from the server.
- **Real-world analogy**: Ordering a coffee — you ask once, and they give it to you once.
- **Use case**: Fetching user profile info by ID.

### 2. Server Streaming
- **Description**: The client sends a single request, and the server responds with a stream of messages.
- **Real-world analogy**: Asking for a playlist and getting songs played one after another.
- **Use case**: Receiving a real-time feed of weather updates for a location.

### 3. Client Streaming
- **Description**: The client sends a stream of requests to the server and waits for a single response.
- **Real-world analogy**: Sending multiple forms/documents and waiting for a single approval or summary.
- **Use case**: Uploading chunks of a file to be processed as one document.

### 4. Bidirectional Streaming
- **Description**: Both the client and server send and receive streams of messages simultaneously.
- **Real-world analogy**: A phone call — both sides talk and listen at the same time.
- **Use case**: Real-time chat, live telemetry, or stock price updates.

---

## Setup

Follow these steps to set up the project:

1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```
2. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```
3. **Install the required packages**:
   ```bash
   pip3 install grpcio
   pip3 install grpcio-tools
   ```
4. **Generate the gRPC code from the `.proto` file**:
   ```bash
   python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto
   ```

## Project Structure
```
.
├── README.md
├── protos
│   └── greet.proto
├── venv
│   └── ... (virtual environment files)
└── ... (other project files)
```

## References
- [gRPC Official Documentation](https://grpc.io/docs/)
- [Protocol Buffers](https://developers.google.com/protocol-buffers)