# gRPC From Python To Python

Click into the numbered directories for all the details and code.

The goal here is to write some code using gRPC, Python and Golang.

## Overview of gRPC

> resource: Below are some quick take aways from gRPC Docs on [gRPC Concepts](https://grpc.io/docs/guides/concepts/).

### Service

- gRPC defines a service. This service could be written in Python. gRPC makes the Python methods available to be called by either *C++, Java (incl. support for Android), Objective-C (for iOS), Python, Ruby, Go, C# and Node.js*
- gRPC uses protocol buffers as the IDL (Interface Development Language)

### Defining the API
- `.proto` file is used to define a service. Once a proto file is compiled it'll generate server and client side code. Using the generated code:
    - The server implements the methods declared by the service.
    - The client has access to call the same methods as the service.
- gRPC is both synchronous and asyncronous. 
- gRPC is written on top of HTTP/2

### RPC request cycle
- Unary RPC
    - client sends one message and receives a single response from the server.
- Streaming
    - Server Streaming
        - client sends one message and receives a stream of messages from the server.
    - Client Streaming
        - client sends a stream of messages, waits and receives a single response from the server.
    - Bidirectional Streaming
        - client and server stream messages back and forth. 
        - Neither have to wait for messages to complete before responding. 
        - Client and server could both send messages asynchronously. 
- Cancelling RPCs
    - Deadlines/Timeouts
        - could be set by both client and server.
    - Termination
        - the client and server make independent and local determinations of whether a call was successful.
- Metadata
    - each request comes with metadata information about the request success or failure.
    - list of key-value pairs
- Channels
    - connection to a gRPC server on a specified host and port
    - used when creating a client stub (or just “client” in some languages)

## Architecture of gRPC
> resource: [Is gRPC the Future of Client-Server Communication?](https://medium.com/@EdgePress/is-grpc-the-future-of-client-server-communication-b112acf9f365)
1. Transport:
    - HTTP/2 is gRPC's transport.
2. Channel:
    - Client connection to a server 
3. Stub:
    - generated by compiling the `.proto` file.
    - provides API methods as they're written