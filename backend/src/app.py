from flask import Flask
from flask_cors import CORS
from backend.src.pathogens import pathogen_routes
from backend.src.users import user_controller

"""
Entry point for Flask application.

To start flask application:
    - cd backend
    - flask run
    
For debug mode (w/ hot reloading):
    - flask run --debug

Last edited by: Harrison Leath
Date: 11/5/24
"""


# config flask app
def create_app():
    app = Flask(__name__)

    cors_config = {
        "methods":["GET", "POST", "PUT", "DELETE", "PATCH"]
    }

    CORS(app, resources={r"/*": cors_config})

    # register blueprints (routes in other files)
    app.register_blueprint(pathogen_routes.bp)
    app.register_blueprint(user_route.bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)