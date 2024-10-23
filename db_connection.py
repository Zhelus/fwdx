#connection file
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = DB_CONNECTION_STRING

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
