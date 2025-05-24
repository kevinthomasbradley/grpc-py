"""
greet_server.py

This script implements the gRPC server for the Greeter service. It handles 
four types of RPC calls: Unary, Server Streaming, Client Streaming, and 
Bidirectional Streaming.

Usage:
- Run this script to start the gRPC server on localhost:50051.
- Ensure the client script is configured to connect to the same address.
"""

from concurrent import futures
import time
import grpc
import greet_pb2
import greet_pb2_grpc

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    """
    Implementation of the Greeter service defined in the greet.proto file.
    Handles the logic for each RPC method.
    """

    def SayHello(self, request, context):
        """
        Unary RPC: Handles a single request and returns a single response.

        Args:
            request (greet_pb2.HelloRequest): The client's request containing a greeting and a name.
            context (grpc.ServicerContext): Provides RPC-specific information.

        Returns:
            greet_pb2.HelloReply: The server's response containing a personalized greeting.
        """
        print("SayHello Request Made:")
        print(request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"
        return hello_reply

    def ParrotSaysHello(self, request, context):
        """
        Server Streaming RPC: Handles a single request and streams multiple responses.

        Args:
            request (greet_pb2.HelloRequest): The client's request containing a greeting and a name.
            context (grpc.ServicerContext): Provides RPC-specific information.

        Yields:
            greet_pb2.HelloReply: A stream of responses containing personalized greetings.
        """
        print("ParrotSaysHello Request Made:")
        print(request)

        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)  # Simulate a delay between responses

    def ChattyClientSaysHello(self, request_iterator, context):
        """
        Client Streaming RPC: Handles a stream of requests and returns a single response.

        Args:
            request_iterator (iterator): A stream of HelloRequest messages from the client.
            context (grpc.ServicerContext): Provides RPC-specific information.

        Returns:
            greet_pb2.DelayedReply: The server's response containing a summary of the received requests.
        """
        delayed_reply = greet_pb2.DelayedReply()
        for request in request_iterator:
            print("ChattyClientSaysHello Request Made:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        """
        Bidirectional Streaming RPC: Handles a stream of requests and streams responses simultaneously.

        Args:
            request_iterator (iterator): A stream of HelloRequest messages from the client.
            context (grpc.ServicerContext): Provides RPC-specific information.

        Yields:
            greet_pb2.HelloReply: A stream of responses containing personalized greetings.
        """
        for request in request_iterator:
            print("InteractingHello Request Made:")
            print(request)

            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name}"
            yield hello_reply

def serve():
    """
    Starts the gRPC server and listens for incoming requests on localhost:50051.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print("Server started on localhost:50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()