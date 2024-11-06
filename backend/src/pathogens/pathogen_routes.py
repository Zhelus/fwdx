from flask import Blueprint, jsonify

from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

"""
This file defines the API endpoints for pathogen use cases.
Make sure the blueprint is attached in "app.py"
"""

bp = Blueprint('pathogen', __name__)


# example query: http://127.0.0.1:5000/v1/pathogen/10632
@bp.route('/v1/pathogen/<id>', methods=['GET'])
def pathogen_get(id: str):
    print("connecting to MongoDB...")
    mongodb_connector = MongoDBConnector(force_ssl=True)
    document = mongodb_connector.fetch_document({"TaxonomyID": id}, CollectionType.PATHOGENS)
    print(document)
    return f"Pathogen returned is: {document}"
