"""
greet_client.py

This script acts as a gRPC client for interacting with the Greeter service. 
It demonstrates the four types of gRPC calls: Unary, Server Streaming, 
Client Streaming, and Bidirectional Streaming.

Usage:
- Run the script and follow the prompts to select the desired RPC call.
- Ensure the gRPC server is running on localhost:50051 before executing this script.
"""

import greet_pb2_grpc
import greet_pb2
import time
import grpc

def get_client_stream_requests():
    """
    Generator function to create a stream of HelloRequest messages for 
    the Client Streaming and Bidirectional Streaming RPCs.

    Yields:
        greet_pb2.HelloRequest: A request containing a greeting and a name.
    """
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        # Create a HelloRequest message with a default greeting and user-provided name
        hello_request = greet_pb2.HelloRequest(greeting="Hello", name=name)
        yield hello_request
        time.sleep(1)  # Simulate a delay between requests

def run():
    """
    Main function to interact with the Greeter service. Prompts the user to 
    select an RPC call and handles the corresponding client logic.

    RPC Options:
    1. Unary RPC: SayHello
    2. Server Streaming RPC: ParrotSaysHello
    3. Client Streaming RPC: ChattyClientSaysHello
    4. Bidirectional Streaming RPC: InteractingHello
    """
    # Establish a connection to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)

        # Display the available RPC options
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both Streaming")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            # Unary RPC: Send a single request and receive a single response
            hello_request = greet_pb2.HelloRequest(greeting="Bonjour", name="YouTube")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)

        elif rpc_call == "2":
            # Server Streaming RPC: Send a single request and receive a stream of responses
            hello_request = greet_pb2.HelloRequest(greeting="Bonjour", name="YouTube")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("ParrotSaysHello Response Received:")
                print(hello_reply)

        elif rpc_call == "3":
            # Client Streaming RPC: Send a stream of requests and receive a single response
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())
            print("ChattyClientSaysHello Response Received:")
            print(delayed_reply)

        elif rpc_call == "4":
            # Bidirectional Streaming RPC: Send and receive streams of messages simultaneously
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print("InteractingHello Response Received:")
                print(response)

if __name__ == "__main__":
    run()