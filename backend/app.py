from flask import Flask, jsonify
from flask_cors import CORS

"""
Entry point for Flask application.

To start flask application:
    - cd backend
    - flask run
    
For debug mode (w/ hot reloading):
    - flask run --debug

Last edited by: Harrison Leath
Date: 10/30/24
"""


def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('config.py')  # Load config

    CORS(app)

    # Register blueprints (for modular routes)
    # app.register_blueprint(main.bp)
    # app.register_blueprint(auth.bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
