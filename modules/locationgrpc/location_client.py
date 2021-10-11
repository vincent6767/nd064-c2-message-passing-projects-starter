import grpc
import location_pb2
import location_pb2_grpc as pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload . . .")

host = '127.0.0.1'
server_port = 30003

channel = grpc.insecure_channel('{}:{}'.format(host, server_port))

stub = pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    id=29,
    person_id=1,
    longitude="2.29782039332223",
    latitude="48.85614465",
    creation_time="2020-07-07 10:37:06.000000"
)

response = stub.Create(location)

print("Got a response! {}", response)