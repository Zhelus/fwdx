from bson import ObjectId
import bcrypt
from flask import session

from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector()

'''
CRUD operations for user accounts. Still need to set the admin rights for these admin functions.
'''

def create_user(user_data):
    # Check if 'password' is provided in user_data
    if 'password' in user_data:
        # Encode and hash the password using bcrypt
        password_bytes = user_data['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

        # Replace the plaintext password with the hashed password
        user_data['password'] = hashed_password.decode('utf-8')

    # Upload the modified user document with hashed password to the database
    return connector.upload_document(user_data, CollectionType.ACCOUNTS)


def get_all_users():
    return connector.fetch_all_documents(CollectionType.ACCOUNTS)


def get_user(user_id):
    return connector.fetch_document({"_id":ObjectId(user_id)}, CollectionType.ACCOUNTS)


def update_user(filter, update):
    return connector.update_document(filter, update, CollectionType.ACCOUNTS)


def delete_user(user_id):
    return connector.delete_document({"_id":ObjectId(user_id)}, CollectionType.ACCOUNTS)


def login_user(email: str, password: str):
    try: # Fetch the user document from MongoDB
        user_document = connector.fetch_document({"email": email}, CollectionType.ACCOUNTS)

        # Check if the user exists and verify the password matches
        if user_document and bcrypt.checkpw(password.encode('utf-8'), user_document.get('password').encode('utf-8')):
            user_id = user_document.get('_id')  # Fetch the user id
            session['user_id'] = str(user_id)  # Begin session for user
            session['logged_in'] = True  # Set boolean flag to true for logged in
            return True, "Login Successful", 200  # Return success status code

        else:
            return False, "Invalid username or password", 401  # Unauthorized access status code

    except Exception as e:
        return False, "An error occurred during login", 500  # Internal server error status code


def logout_user(user_id):
    #Remove user info from session
    session.pop(user_id, None)
    session.pop('logged_in', None)


def change_password(user_id, new_password):
    # Ensure user_id is a valid ObjectId
    if not ObjectId.is_valid(user_id):
        return "Invalid user ID"

    # Hash the new password before storing it
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    # Create the filter and update dictionaries
    filter = {"_id": ObjectId(user_id)}
    update = {"$set": {"password": hashed_password}}

    # Update the document in the ACCOUNTS collection
    result = connector.update_document(filter, update, CollectionType.ACCOUNTS)
    return result


def register_user(user_data):
    return connector.register_document({CollectionType.ACCOUNTS})

