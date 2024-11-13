from flask import Blueprint, jsonify, request

from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType
from backend.src.reports.report import Report



"""
This file defines the API endpoints for report use cases.
"""
bp = Blueprint('report', __name__)


"""
Method to get a report using the report ID
    - Inputs: id (string)
    - Outputs: the report with the specified id
"""
@bp.route('/v1/report/<id>', methods=['GET'])
def get_report(id: str):
    print("connecting to MongoDB...")
    # Get the report with the corresponding report ID
    mongodb_connector = MongoDBConnector(force_ssl=True)
    report = mongodb_connector.fetch_document({"report_id": id}, CollectionType.REPORTS)
    report = _object_id_to_string(report)
    return jsonify({'report': report})


"""
Method to save a new report to MongoDB 
    - Inputs: new_report (dict, passed in the request body/request.json)
    - Outputs: the newly created report
"""
@bp.route('/v1/report', methods=['POST'])
def create_new_report():
    print("connecting to MongoDB...")
    # Extract report data from the request
    new_report = request.json
    # Save the new report
    mongodb_connector = MongoDBConnector(force_ssl=True)
    document = mongodb_connector.upload_document(new_report, CollectionType.REPORTS)
    return f"Report returned is: {document}"


"""
Method to update a report specified by the id
    - Inputs: id (string), updated_report_data (dict, passed in the request body/request.json)
    - Outputs: the updated report
"""
@bp.route('/v1/report/<id>', methods=['PUT'])
def update_report(id: str):
    print("connecting to MongoDB...")
    # Use the report ID to specify the report to be updated
    filter = { 'report_id': id }
    # Set the fields to be updated
    updated_report_data = request.json
    update = { "$set": updated_report_data }
    # Save the updated report data
    mongodb_connector = MongoDBConnector(force_ssl=True)
    document = mongodb_connector.update_document(filter, update, CollectionType.REPORTS)
    return f"Report returned is: {document}"


"""
 Method to deleted the report specified by the id
    - Inputs: id (string)
    - Outputs: the report that has been deleted
"""
@bp.route('/v1/report/<id>', methods=['DELETE'])
def delete_report(id: str):
    print("connecting to MongoDB...")
    # Get the report to be deleted, using the report's ID
    mongodb_connector = MongoDBConnector(force_ssl=True)
    report_to_delete = mongodb_connector.fetch_document({"report_id": id}, CollectionType.REPORTS)
    # Delete the report
    document = mongodb_connector.delete_document(report_to_delete, CollectionType.REPORTS)
    return f"Report returned is: {document}"

"""
Method to get all reports from the 'Reports' collection
    - Inputs: none
    - Outputs: all reports in the 'Reports' collection
"""
@bp.route('/v1/report/all', methods=['GET'])
def get_all_reports():
    print("connecting to MongoDB...")
    # Get all reports from the collection
    mongodb_connector = MongoDBConnector(force_ssl=True)
    cursor = mongodb_connector.fetch_all_documents(CollectionType.REPORTS, filter={})
    # Format each report to be returned
    returned_reports = []
    for report in cursor:
        report = _object_id_to_string(report)
        returned_reports.append(report)
    # Return all reports formatted as JSON
    return jsonify({'reports': returned_reports})

"""
Helper method to translate a report's MongoDB 'ObjectId' to a string (needed to convert report data to JSON)
    - Inputs: report (dict with '_id' as an ObjectId)
    - Outputs: report (dict with '_id' as a string)
"""
def _object_id_to_string(report):
        report['_id'] = str(report['_id'])
        return report
