from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from .user_service import create_user, get_user, update_user, delete_user, change_password, register_user, login_user, \
    logout_user, get_all_users
from ...definitions import API_VERSION

bp = Blueprint('users', __name__)


#example query: http://127.0.0.1:5000/v1/users/create
@bp.route(f'/{API_VERSION}/users/create', methods=['POST'])
def api_create_user():
    user_data = request.get_json()
    document = create_user(user_data)
    return f"User created is: {document}"


@bp.route(f'/{API_VERSION}/users/get_all_users', methods=['GET'])
def api_get_all_users():
    try:
        cursor = get_all_users()
        returned_users = []
        for user in cursor:
            user = _object_id_to_string(user)
            returned_users.append(user)
        # Return all users formatted as JSON
        return jsonify({'users': returned_users})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
      
      
"""
Helper method to tranlsate a user's MongoDB 'ObjectId' to a string
 - Inputs: user (dict with '_id' as an ObjectId)
 - Outputs: user (dict with '_id' as a String
"""
def _object_id_to_string(user):
    user['_id'] = str (user['_id'])
    return user

def _string_to_object_id(user_id):
    user_id = ObjectId(user_id)
    return user_id

#example query: http://127.0.0.1:5000/v1/users/get/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/users/get/<string:user_id>', methods=['GET'])
def api_get_user(user_id):
    try:
        user = get_user(user_id)
        user = _object_id_to_string(user)
        return jsonify({'user': user})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



#example query: http://127.0.0.1:5000/v1/users/update/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/users/update/<string:user_id>', methods=['PUT'])
def api_update_user(user_id):

    #user_id = _string_to_object_id(user_id)
    filter = { 'user_id': user_id}
    updated_user_data = request.get_json()
    update = { "$set": updated_user_data}
    document = update_user(filter, update)
    return f"User updated to: {document}"


# example query: http://127.0.0.1:5000/v1/users/delete/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/users/delete/<string:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    document = delete_user(user_id)
    return f"User deleted is: {document}"


@bp.route(f'/{API_VERSION}/users/login', methods=['POST'])
def api_login_user():
    email = request.json['email']
    password = request.json['password']
    success, message, status = login_user(email, password)

    if success:
        return jsonify({"message": message}), status
    else:
        return jsonify({"error": message}), status


@bp.route(f'/{API_VERSION}/users/logout/<string:user_id>', methods=['POST'])
def api_logout_user(user_id):
    logout_user(user_id)
    return f"User is logged out"


@bp.route(f'/{API_VERSION}/users/register', methods=['GET', 'POST'])
def api_register_user():
    user_data = request.get_json()
    document = register_user(user_data)
    return f"User is registered is: {document}"

  
# example query: http://127.0.0.1:5000/v1/users/changepassword/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/users/changepassword/<string:user_id>', methods=['PUT'])
def api_change_password(user_id):
    new_password = request.get_json().get('newPassword')
    return change_password(user_id, new_password)