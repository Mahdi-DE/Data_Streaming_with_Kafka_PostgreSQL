
# Data Streaming with Kafka & PostgrSQL

## Services Overview:
[![Docker Image](https://img.shields.io/badge/Docker-blue.svg)](https://hub.docker.com)


The provided Docker Compose file defines a multi-container application. It specifies services for Zookeeper, three Kafka brokers, a PostgreSQL database, and a pgAdmin interface. The services are connected through a shared network called postgres-db-network.

[![Zookeeper](https://img.shields.io/badge/Zookeeper-blue.svg)](https://kafka.apache.org)


Zookeeper coordinates distributed applications by providing reliable data synchronization. It is crucial for managing the Kafka brokers.
- Port 2181 to the host. 

[![Kafka Broker](https://img.shields.io/badge/Kafka%20Broker-blue.svg)](https://kafka.apache.org)

Three Kafka brokers are configured to create a robust and scalable message queue system. Each broker communicates seamlessly with Zookeeper and the other brokers, and they each expose unique internal and external ports to prevent conflicts and dependencies. Additionally, each Kafka broker relies on Zookeeper, necessitating that Zookeeper starts before the brokers.


[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue.svg)](https://www.postgresql.org)

- Port 5432 is exposed to the host.
- Environment Variables include the default credentials for the database user.
- Volumes ensure data persistence by mapping a local directory to the container's data directory.


[![pgAdmin](https://img.shields.io/badge/pgAdmin-blue.svg)](https://www.pgadmin.org)

pgAdmin provides a web-based interface to manage and interact with the PostgreSQL database. 
- Port 16543 is exposed to the host.
- Environment Variables are set to establish default login credentials for pgAdmin.
- Volume mappings ensure that configuration files are preserved, enabling persistent settings.
- You can access the pgAdmin web interface at http://localhost:16543.

## Configuration Files:

- Database.ini file is for a PostgreSQL that contains the necessary details to connect to a PostgreSQL database.

- Config.py file is Python script that reads the configuration from Database.ini and returns a dictionary with the connection parameters.

- Server.json file configures the pgAdmin tool to connect to the PostgreSQL server.

- Kafka Producer file generates random user data comprising an address, age, and phone number, serialized into JSON format, and sends it to a Kafka topic named 'test'. It utilizes the KafkaProducer class from the Kafka library, configured to connect to the Kafka broker on 'localhost:9092', with a periodic message production interval of 20 seconds. Random data is generated using Python's 'random' and 'string' modules, ensuring a varied dataset for testing and development purposes.

- Kafka consumer reads messages from the test topic and inserts the received data into a PostgreSQL database. It ensures that the database table exists and then continuously processes incoming messages.

## Support

For support, please contact me at nematshahi.mahdi@gmail.com.

