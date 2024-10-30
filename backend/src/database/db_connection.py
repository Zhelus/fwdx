import os

import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from definitions import ENV_DIR

"""
Temporary wrapper around MongoDB
Last edited by: Harrison Leath
Date: 10/30/24
"""

class MongoDBConnector:
    def __init__(self):
        load_dotenv(ENV_DIR)
        self.uri = os.getenv('DB_CONNECTION_STRING')

        # self.client = self.connect()
        self.client = self.connect_ssl()

    def connect(self):
        try:
            client = MongoClient(self.uri, server_api=ServerApi('1'))
        except Exception as e:
            print("Error connecting to MongoDB:", e)

        return client

    def connect_ssl(self):
        # Use the certifi library to get the path of the CA certificate
        ca = certifi.where()

        try:
            # Create a MongoClient instance and specify the CA certificate path
            client = MongoClient(self.uri, server_api=ServerApi('1'), tlsCAFile=ca)

        except Exception as e:
            print("Error connecting to MongoDB:", e)

        return client

    def ping(self):
        try:
            self.client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("Error connecting to MongoDB:", e)
