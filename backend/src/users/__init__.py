from flask import Flask
from .user_route import users_blueprint

def init_app(app: Flask):
    app.register_blueprint(users_blueprint, url_prefix='/v1')
