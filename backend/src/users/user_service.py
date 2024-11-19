import hashlib
from bson import ObjectId
import bcrypt
from flask import url_for, redirect, session
from mongoengine import connect

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

def login_user(email: str, password: str):
    # Hash the password for comparison
    # hashed_password = hashlib.sha256(password.encode()).hexdigest()
    hashed_password = "123456789"

    # Fetch the user document from MongoDB
    user_document = connector.fetch_document({"email": email}, CollectionType.ACCOUNTS)

    # Check if the user exists and the password matches
    if user_document and user_document.get('password') == hashed_password:
        user_id = user_document.get('_id')    #Fetch the user id
        session['user_id'] = str(user_id)        #Begin session for user
        session['logged_in'] = True           #Set boolean flag to true for logged in
        return True, "Login Successful"
    else:
        return False, "Invalid username or password"


def logout_user():
    #Remove user info from session
    session.pop('user_id', None)
    session.pop('logged_in', None)


def change_password(user_id, new_password):
    filter = {"_id": ObjectId(user_id)}
    update = {"$set": new_password}
    return connector.update_document(filter, update, CollectionType.ACCOUNTS)

def register_user(user_data):
    return connector.register_document({CollectionType.ACCOUNTS})

