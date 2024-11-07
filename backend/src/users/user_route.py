from flask import Blueprint, request
from .user_service import create_user, get_user, update_user, delete_user, change_password


bp = Blueprint('users', __name__)


#example query: http://127.0.0.1:5000/v1/users/create
@bp.route('/v1/users/create', methods=['POST'])
def api_create_user():
    user_data = request.get_json()
    document = create_user(user_data)
    return f"User created is: {document}"


#example query: http://127.0.0.1:5000/v1/users/get/6722541f635480d44cf29db4
@bp.route('/v1/users/get/<string:user_id>', methods=['GET'])
def api_get_user(user_id):
    document = get_user(user_id)
    return f"User returned is: {document}"


#example query: http://127.0.0.1:5000/v1/users/update/6722541f635480d44cf29db4
@bp.route('/v1/users/update/<string:user_id>', methods=['PUT'])
def api_update_user(user_id):
    user_data = request.get_json()
    document = update_user(user_id, user_data)
    return f"User updated to: {document}"


#example query: http://127.0.0.1:5000/v1/users/delete/6722541f635480d44cf29db4
@bp.route('/v1/users/delete/<string:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    document = delete_user(user_id)
    return f"User deleted is: {document}"



'''
On hold until user registration, login, and forgot password are built out.
'''
#example query: http://127.0.0.1:5000/v1/users/changepassword/6722541f635480d44cf29db4
@bp.route('/v1/users/changepassword/<string:user_id>', methods=['PATCH'])
def api_change_password(user_id):
    new_password = request.get_json().get('newPassword')
    return change_password(user_id, new_password)

