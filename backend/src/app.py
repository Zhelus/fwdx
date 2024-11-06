from flask import Flask
from flask_cors import CORS
from backend.src.pathogens import pathogen_routes

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

    CORS(app)

    # register blueprints (routes in other files)
    app.register_blueprint(pathogen_routes.bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
