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

app = Flask(__name__)
CORS(app)

"""
Debug endpoints, actual endpoints will be created in the existing folders.
"""


@app.route("/api/debug")
def debug():
    return jsonify(message="Debug message :)")


if __name__ == '__main__':
    app.run(debug=True)
