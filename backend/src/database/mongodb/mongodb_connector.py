"""
Temporary wrapper around MongoDB

Last edited by: Kyle Stagner
Date: 2024/11/03
"""

import os

import certifi
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from backend.src.helper.collection_type import CollectionType
from backend.src.helper.environment import Environment

"""
***for backend.definitions to work as designed***
config.env file must contain PYTHONPATH=./ so that the project root is included in sys path
#also be sure to include "python.envFile": "${workspaceFolder}/config.env", in your .vscode/settings.json file
"""


class MongoDBConnector:

    # NOTE: initialization of object creates new connection to MongoDB, may want to create a singleton instead
    def __init__(self, force_ssl: bool = False):
        self.env = Environment()

        self.uri = self.env.DB_CONNECTION_STRING

        if self.uri is None:
            raise ValueError("[MongoDB_Connector] URI not set, check config.env file")

        if force_ssl:
            self._connect_ssl()
        else:
            self._connect()

        self.database = self.client[self.env.DB_NAME]

    def _connect(self):
        client = None
        try:
            client = MongoClient(self.uri, server_api=ServerApi('1'))
        except Exception as e:
            print("[MongoDBConnector] Error connecting to MongoDB (SSL not forced):", e)

        self.client = client

    def _connect_ssl(self):
        client = None

        # Use the certifi library to get the path of the CA certificate
        ca = certifi.where()
        try:
            # Create a MongoClient instance and specify the CA certificate path
            client = MongoClient(self.uri, server_api=ServerApi('1'), tlsCAFile=ca)

        except Exception as e:
            print("[MongoDBConnector] Error connecting to MongoDB (SSL forced):", e)

        self.client = client

    def upload_document(self, document: dict, collection: CollectionType):
        collection = self.database[collection.value]
        return collection.insert_one(document)

    def fetch_document(self, document: dict, collection: CollectionType):
        collection = self.database[collection.value]
        result = collection.find_one(document)
        return result

    def fetch_documents(self, limit: int, collection: CollectionType):
        collection = self.database[collection.value]
        result = collection.find().sort('_id', pymongo.DESCENDING).limit(limit)
        return result

    def delete_document(self, document: dict, collection: CollectionType):
        collection = self.database[collection.value]
        result = collection.find_one_and_delete(document)
        return result

    def update_document(self, filter, update, collection: CollectionType):
        result = self.database[collection.value].update_one(filter, update)
        return result

    def fetch_all_documents(self, collection: CollectionType, filter: dict = {}):
        result = self.database[collection.value].find(filter)
        return result

    def create_collection(self, collection: CollectionType):
        collection = self.database.create_collection(collection.value)
        print(f"Created New Collection:\n{collection}\n{collection.name}")

    def fetch_all_documents_by_filter(self, filter: dict, collection: CollectionType):
        """
        Fetch all documents matching the filter.
        """
        collection = self.database[collection.value]
        return list(collection.find(filter))

    def ping(self):
        try:
            self.client.admin.command("ping")
            print("[MongoDBConnector] Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("[MongoDBConnector] Error connecting to MongoDB:", e)

    def get_connection_uri(self):
        return self.uri

    def close_connection(self):
        """Close the MongoDB connection gracefully."""
        if self.client:
            self.client.close()
            print("[MongoDBConnector] Connection to MongoDB closed.")
