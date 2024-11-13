from bson import ObjectId
import bcrypt
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector()

'''
CRUD operations for user accounts. Still need to set the admin rights for these admin functions.
'''

def create_user(user_data):
    return connector.upload_document(user_data, CollectionType.ACCOUNTS)


def get_user(user_id):
    return connector.fetch_document({"_id":ObjectId(user_id)}, CollectionType.ACCOUNTS)


def update_user(user_id, user_data):
    user_filter = {"_id": ObjectId(user_id)}
    # Prepare the update statement, using $set to specify the fields to update
    update = {"$set": user_data}
    return connector.update_document(user_filter, update, CollectionType.ACCOUNTS)


def delete_user(user_id):
    return connector.delete_document({"_id":ObjectId(user_id)}, CollectionType.ACCOUNTS)


'''
On hold until user registration, login, and forgot password are built out
'''

def change_password(user_id, new_password):
    filter = {"_id": ObjectId(user_id)}
    update = {"$set": new_password}
    return connector.update_document(filter, update, CollectionType.ACCOUNTS)

def hash_password(self, password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def register_user():
    return connector.register_document({CollectionType.ACCOUNTS})

def login_user():
    return connector.login_document({CollectionType.ACCOUNTS})