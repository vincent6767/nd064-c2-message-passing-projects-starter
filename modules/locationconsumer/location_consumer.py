import json, psycopg2, os, sys
from kafka import KafkaConsumer

topic = "people_location"
kafka_server = "kafka-service:9092"
consumer = KafkaConsumer(topic, bootstrap_servers=kafka_server)

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

try:
    connection = psycopg2.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name
    )
    cursor = connection.cursor()

    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
        payload = json.loads(message.value.decode('utf-8'))
        print("Message payload: {}, Person id: {}".format(payload, payload['person_id'])) # to be removed later.

        try: 
            coordinate = '010100000000ADF9F197925EC0FDA19927D7C64240' # TODO: calculate this based on the longitude and latitude

            postgres_insert_query = "INSERT INTO location (id, person_id, coordinate, creation_time) VALUES (%s, %s, %s, %s)"
            record_to_insert = (payload['id'], payload['person_id'], coordinate , payload['creation_time'])

            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()

            print(cursor.rowcount, " record inserted successfully into location table")
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into location table", error)
            print("Rolling back the command . . .")
            connection.rollback()
            print("Continue listening . . .")
except KeyboardInterrupt:
    print("Detected signal exit. Exiting application . . .")
except (psycopg2.Error) as error:
    print("Failed to connect to the PostgreSQL", error)
    print("Application exit")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgresSQL connection closed")

