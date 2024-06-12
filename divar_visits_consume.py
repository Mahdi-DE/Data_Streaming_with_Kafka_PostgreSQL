from kafka import KafkaConsumer
import json
import psycopg2
from psycopg2 import sql
from config import config
# connection = psycopg2.connect(host="localhost", port="5432", database="", user="", password="")

consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], 
                         auto_offset_reset='earliest', enable_auto_commit=True, 
                         group_id='my-group-id', value_deserializer=lambda x: json.loads(x.decode('utf-8')))


create_table_query = """CREATE TABLE IF NOT EXISTS public.customers (customer_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                address VARCHAR(255), age INT, phone_number VARCHAR(20));"""
def connect():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        crsr = connection.cursor()
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)

        for c in consumer:

            crsr.execute(create_table_query)
            connection.commit()

            customer_data = (c.value['address'],
                             c.value['age'],c.value['phone_number'])

            insert_data_query = """INSERT INTO public.customers (address, age, phone_number) 
                                   VALUES (%s, %s, %s);"""

            crsr.execute(insert_data_query, customer_data)
            connection.commit()
            print(customer_data)

        crsr.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')


if __name__ == "__main__":
    connect()




