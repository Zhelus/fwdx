import os

from flask import Flask
from flask_cors import CORS
from backend.src.pathogens import pathogen_routes
from backend.src.users import user_controller
from backend.src.reports import report_controller
from backend.src.reagents import product_controller
from dotenv import load_dotenv


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
    # Load the environment variables from 'config.env'
    load_dotenv('config.env')

    # Access the API key
    app.secret_key = os.getenv('API_KEY')

    if not app.secret_key:
        raise RuntimeError("Runtime error with API key")

    CORS(app, supports_credentials=True, resources={r"/*": cors_config})

    # register blueprints (routes in other files)
    app.register_blueprint(pathogen_routes.bp)
    app.register_blueprint(user_controller.bp)
    app.register_blueprint(report_controller.bp)
    app.register_blueprint(product_controller.bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
