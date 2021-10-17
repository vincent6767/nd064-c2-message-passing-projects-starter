import grpc
import time
from concurrent import futures
from kafka import KafkaProducer
from kafka import KafkaTimeoutError
import location_pb2_grpc
import location_pb2

class LocationService(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }

        topic_name = 'people_location'
        kafka_server = 'kafka-service:9092'
        producer = KafkaProducer(bootstrap_servers=kafka_server)
        print("Created producer")
        try:
            producer.send(topic_name, "Hello, World!")
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")

        print("Sent a message to Kafka")

        return location_pb2.LocationMessage(**request_value)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationService(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("Server starting on port 5000 . . .")
    serve()