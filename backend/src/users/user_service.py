from .user_model import User
from flask import jsonify
from ..database.db_connection import MongoDBConnector

connector = MongoDBConnector()
client = connector.connect()
fwdx = client["FWDX_Database"]
accounts = fwdx["Accounts"]

def create_user(data):
    """
    Creates a new user in the database from the provided data.

    Parameters:
        data (dict): A dictionary containing the user data. Expected keys are:
                     'first_name', 'last_name', 'phone_number', 'email',
                     'role', 'department', and 'access_level'.

    Returns:
        tuple: A tuple containing a Flask Response (jsonify) representing the newly created user
               and an HTTP status code. Returns 201 if successful; otherwise, it returns an error
               code along with an error message.

    This function is intended to be called by an API endpoint to handle a POST request
    for creating a new user in the database.
    """
    try:
        user = User(**data).save()
        #accounts.insert_one(user)
        return jsonify(user.to_json()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def get_user(user_id):
    """
    Retrieves a user by their unique ID from the database.

    Parameters:
        user_id (str): The unique identifier of the user to retrieve.

    Returns:
        Flask Response: JSON representation of the user if found, otherwise returns a JSON error
                        message and a 404 status code indicating the user was not found.

    This function supports API endpoint operations that require fetching user details.
    """
    try:
        user = User.objects(id=user_id).get()
        #accounts.find_one(user)
        return jsonify(user.to_json())
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

def update_user(user_id, data):
    """
    Updates an existing user's data in the database.

    Parameters:
        user_id (str): The unique identifier of the user to update.
        data (dict): A dictionary containing updates to user fields such as first name, last name,
                     phone number, email, role, department, and access level.

    Returns:
        Flask Response: JSON representation of the updated user or an error message and status code
                        if the user does not exist.

    This function is used by API endpoints handling PUT requests for user updates.
    """
    try:
        user = User.objects(id=user_id).get()
        user.update(**data)
        return jsonify(user.reload().to_json())
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

def delete_user(user_id):
    """
    Deletes a user from the database by their ID.

    Parameters:
        user_id (str): The unique identifier of the user to delete.

    Returns:
        Flask Response: JSON confirmation message if the deletion was successful, or a JSON error
                        message and a 404 status code if the user does not exist.

    This function facilitates API endpoint operations for DELETE requests targeting user removal.
    """
    try:
        user = User.objects(id=user_id).get()
        user.delete()
        return jsonify({'message': 'User deleted'}), 204
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

def change_password(user_id, new_password):
    """
    Changes the password for an existing user identified by their ID.

    Parameters:
        user_id (str): The unique identifier of the user whose password is to be changed.
        new_password (str): The new password to set for the user.

    Returns:
        Flask Response: JSON message indicating the password update status. If the user does not
                        exist, it returns a JSON error message and a 404 status code.

    Note:
        In production, ensure to hash the password before storing it to secure user data.

    This function is designed to support PATCH requests from API endpoints intended to change user passwords.
    """
    try:
        user = User.objects(id=user_id).get()
        user.update(password=new_password)  # Add password hashing in a real implementation
        return jsonify({'message': 'Password updated successfully'})
    except User.DoesNotExist:
        return jsonify({'error': 'User not found'}), 404

