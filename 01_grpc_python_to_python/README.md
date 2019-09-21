# 01_grpc_python_to_python
Small app, written in Python, that uses gRPC to communicate with Python. 
The app simply reverses the order of a string. 
The main goal here is to create a structure for using gRPC.
Ideas here are from hours of google search results.


## Terminal Commands
- `$make run`
    - will create a new path and generate ProtoBuf files:
        - `/python/proto/reverse_service/proto/`
    - will spin up a Python server and a Python client. 
    - the client will send requests to the server every 4 seconds.
    - to kill either, press `ctl z`.

- `$make test`
    - Tests use the gRPC authored testing library, `grpc_testing`. 
    The library mocks the server and does not require, a server to be spun up.


For larger projects it is recommended to have a single repo for all the proto files. 
There you would have a shell script that could generate language specific gRPC files. 
Once files are generated, you could package it. (PyPI for Python for example)