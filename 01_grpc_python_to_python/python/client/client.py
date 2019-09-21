import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import grpc
import time
from proto.reverse_service import reverse_pb2 as pb
from proto.reverse_service import reverse_pb2_grpc as pb_grpc


class ReverserClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # instantiate a communication channel
        self.channel = grpc.insecure_channel('localhost:5005')

        # bind the client to the server channel
        self.stub = pb_grpc.ReverserStub(self.channel)

    def run_reverse(self):
        request_string = pb.RequestString(request_string='this is a test')
        return self.stub.Reverse(request_string)


if __name__ == '__main__':
    pc = ReverserClient()
    while True:
        print(pc.run_reverse())
        time.sleep(4)
