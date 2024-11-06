import os
from dotenv import load_dotenv

from backend.definitions import ENV_DIR

"""
I would like to implement value checking in this class rather than making every file
using a environment variable have to check...
"""


class Environment:
    def __init__(self):
        load_dotenv(ENV_DIR)

        self.DB_CONNECTION_STRING = os.getenv('DB_CONNECTION_STRING')
        self.DB_NAME = os.getenv('DB_NAME')
