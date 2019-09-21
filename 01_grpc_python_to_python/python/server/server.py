import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import grpc
import time
from concurrent import futures

from tools import reverse
from proto.reverse_service import reverse_pb2 as pb
from proto.reverse_service import reverse_pb2_grpc as pb_grpc


class ReverserService(pb_grpc.ReverserServicer):
    """
    gRPC server
    """

    def __init__(self):
        self.server_port = '5005'

    def Reverse(self, request, context):
        """
        running the Reverse object declared in the proto file
        """
        original_string = request.request_string
        reversed_string = reverse(original_string)

        return pb.ResponseString(
            original_string=original_string,
            reversed_string=reversed_string
        )

    def start_server(self):
        # declare a server object with desired number of thread pool workers
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))

        # add ReverserService service to the server object
        pb_grpc.add_ReverserServicer_to_server(ReverserService(), server)

        # bind the server to the port
        server.add_insecure_port('[::]:%s' % self.server_port)

        # start the server
        server.start()
        print('Reverser python-server running')

        try:
            # need an infinite loop since the above code is non blocking
            # and if I don't do this the program will exit
            while True:
                time.sleep(60 * 60 * 60)
        except KeyboardInterrupt:
            server.stop(0)
            print('Reverser python-server stopped ...')


if __name__ == '__main__':
    curr_server = ReverserService()
    curr_server.start_server()
