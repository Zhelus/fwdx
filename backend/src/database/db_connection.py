"""
Temporary wrapper around MongoDB

Last edited by: Kyle Stagner
Date: 2024/11/03
"""

import os

import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

"""
***for backend.definitions to work as designed***
config.env file must contain PYTHONPATH=./ so that the project root is included in sys path
#also be sure to include "python.envFile": "${workspaceFolder}/config.env", in your .vscode/settings.json file
"""

from backend.definitions import ENV_DIR

class MongoDBConnector:
    def __init__(self):
        load_dotenv(ENV_DIR)
        self.uri = os.getenv('DB_CONNECTION_STRING')

        if self.uri is None:
            raise ValueError("Missing DB_CONNECTION_STRING. Is \"config.env\" in the right place?")

        # self.client = self.connect()
        self.client = self.connect_ssl()
        self.db = self.client['FWDX_Database']  # Replace 'your_database' with the name of your actual database


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

    def get_connection_uri(self):
        return self.uri         

    def close_connection(self):
        """Close the MongoDB connection gracefully."""
        if self.client:
            self.client.close()
            print("Connection to MongoDB closed.")

# Example usage for testing the connection
if __name__ == "__main__":
    connector = MongoDBConnector()
    connector.close_connection()
    
# debug code
# connector = MongoDBConnector()
# connector.ping()
