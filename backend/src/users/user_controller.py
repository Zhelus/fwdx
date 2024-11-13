from flask import Blueprint, request
from .user_service import create_user, get_user, update_user, delete_user, change_password, register_user, login_user
from ...definitions import API_VERSION

bp = Blueprint('users', __name__)


#example query: http://127.0.0.1:5000/v1/users/create
@bp.route(f'/{API_VERSION}/users/create', methods=['POST'])
def api_create_user():
    user_data = request.get_json()
    document = create_user(user_data)
    return f"User created is: {document}"


#example query: http://127.0.0.1:5000/v1/users/get/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/users/get/<string:user_id>', methods=['GET'])
def api_get_user(user_id):
    document = get_user(user_id)
    return f"User returned is: {document}"


#example query: http://127.0.0.1:5000/v1/users/update/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/update/<string:user_id>', methods=['PUT'])
def api_update_user(user_id):
    user_data = request.get_json()
    document = update_user(user_id, user_data)
    return f"User updated to: {document}"


#example query: http://127.0.0.1:5000/v1/users/delete/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/users/delete/<string:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    document = delete_user(user_id)
    return f"User deleted is: {document}"


@bp.route(f'{API_VERSION}/users/register', methods=['GET', 'POST'])
def api_register_user():
    user_data = request.get_json()
    document = register_user(user_data['email'], user_data['password'])
    return f"User is registered is: {document}"


@bp.route(f'{API_VERSION}/users/login', methods=['GET', 'POST'])
def api_login_user():
    document = login_user()
    return f"User is logged in: {document}"

'''
On hold until user registration, login, and forgot password are built out.
'''

#example query: http://127.0.0.1:5000/v1/users/changepassword/6722541f635480d44cf29db4
@bp.route(f'/{API_VERSION}/users/changepassword/<string:user_id>', methods=['PATCH'])
def api_change_password(user_id):
    new_password = request.get_json().get('newPassword')
    return change_password(user_id, new_password)

