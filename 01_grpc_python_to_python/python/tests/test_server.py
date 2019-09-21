import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import grpc
import grpc_testing
from google.protobuf import json_format

from proto.reverse_service import reverse_pb2 as pb
from server.server import ReverserService


def get_test_server():
    """Define test server"""
    service_names = {
        pb.DESCRIPTOR.services_by_name['Reverser']: ReverserService()
    }
    test_server = grpc_testing.server_from_dictionary(service_names, grpc_testing.strict_real_time())
    return test_server


def test_server_request():
    request_string = 'this is a test'
    request = pb.RequestString(request_string=request_string)
    test_server = get_test_server()
    services = pb.DESCRIPTOR.services_by_name
    descriptor = (services['Reverser'].methods_by_name['Reverse'])
    response, metadata, code, details = test_server.invoke_unary_unary(
        method_descriptor=descriptor,
        invocation_metadata={},
        request=request,
        timeout=1
    ).termination()

    # confirm response code
    assert code == grpc.StatusCode.OK

    # confirm results
    response_dict = json_format.MessageToDict(response, preserving_proto_field_name=True)
    assert response_dict['original_string'] == request_string
    assert response_dict['reversed_string'] == "tset a si siht"
