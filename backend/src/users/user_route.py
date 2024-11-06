from flask import Blueprint, request
from .user_service import create_user, get_user, update_user, delete_user, change_password

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/users', methods=['POST'])
def api_create_user():
    """
   API endpoint to create a new user.

   Expects a JSON payload with user data. Uses the create_user service to add
   the user to the database.

   Returns:
       JSON response with the new user's data and a status code.
   """
    data = request.get_json()
    return create_user(data)


@users_blueprint.route('/users/<string:user_id>', methods=['GET'])
def api_get_user(user_id):
    """
    API endpoint to retrieve a specific user's details by their ID.

    Parameters:
        user_id (str): The unique identifier of the user.

    Returns:
        JSON response containing the user's data if found, otherwise a 404 error
        if no user is found with the provided ID.
    """
    return get_user(user_id)


@users_blueprint.route('/users/<string:user_id>', methods=['PUT'])
def api_update_user(user_id):
    """
    API endpoint to update a user's details.

    Parameters:
        user_id (str): The unique identifier of the user to update.
    Expects:
        A JSON payload with one or more user attributes to update, such as first name,
        last name, phone number, email, role, department, or access level.

    Returns:
        JSON response with the updated user's data if successful, otherwise an error
        message and status code.
    """
    data = request.get_json()
    return update_user(user_id, data)


@users_blueprint.route('/users/<string:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    """
    API endpoint to delete a user.

    Parameters:
        user_id (str): The unique identifier of the user to delete.

    Returns:
        JSON response with a confirmation message if the deletion was successful,
        otherwise an error message and status code.
    """
    return delete_user(user_id)


@users_blueprint.route('/users/<string:user_id>/password', methods=['PATCH'])
def api_change_password(user_id):
    """
    API endpoint to change a user's password.

    Parameters:
        user_id (str): The unique identifier of the user whose password is to be changed.
    Expects:
        A JSON payload with the new password.

    Returns:
        JSON response with a success message if the password was changed successfully,
        otherwise an error message and status code.
    """
    new_password = request.get_json().get('newPassword')
    return change_password(user_id, new_password)
