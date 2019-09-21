#!/bin/bash
# Use gRPC Tools to generate Python ProtoBuf files

python -m grpc_tools.protoc -I. --python_out=python/ --grpc_python_out=python/ proto/reverse_service/reverse.proto
touch python/proto/__init__.py
touch python/proto/reverse_service/__init__.py