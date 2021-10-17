from kafka import KafkaConsumer

topic = "people_location"
kafka_server = "kafka-service:9092"
consumer = KafkaConsumer(topic, bootstrap_servers=kafka_server)

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

