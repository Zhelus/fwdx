from flask import Blueprint, jsonify

"""
This file defines the API endpoints for pathogen use cases.
Make sure the blueprint is attached in "app.py"
"""

bp = Blueprint('pathogen', __name__)


@bp.route('/v1/pathogen', methods=['GET'])
def pathogen_get():
    return "Your first pathogen is here!"


@bp.route('/v1/debug', methods=['GET'])
def debug():
    return "this was a test"
