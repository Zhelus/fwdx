#connection file
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

def load_env_file(filepath):
    # Open the .env file and automatically close it after reading
    with open(filepath) as file:
        for line in file:
            # Strip leading/trailing whitespace and skip empty lines or comments
            line = line.strip()
            if line and not line.startswith('#'):
                # Split the line into key and value by the first '='
                key, value = line.split('=', 1)
                
                # Set the key-value pair as an environment variable
                os.environ[key] = value
# Load environment variables from the mongodb.env file
load_env_file('mongodb.env')

# Access the variables from the environment
db_admin_account = os.getenv('DB_ADMIN_ACCOUNT')
db_admin_password = os.getenv('DB_ADMIN_PASSWORD')
db_connection_string = os.getenv('DB_CONNECTION_STRING')
# end load


print(f"Imported Connection String: {db_connection_string}")

uri = db_connection_string

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Choose sample database
db = client["sample_mflix"]

# Choose some sample collections, this could be like reagents or users etc
comments = db["comments"]
embedded_movies = db["embedded_movies"]

# Find a entry 
# print(comments.)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
