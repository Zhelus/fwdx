import pytest
import mongomock
from flask import Flask
from flask_testing import TestCase
from backend.src.users.user_service import create_user, get_user
from backend.src.database.db_connection import MongoDBConnector
from mongoengine import connect, get_connection, disconnect



# connector = MongoDBConnector()
# client = connector.connect()
# fwdx = client["FWDX_Database"]
# accounts = fwdx["Accounts"]

class TestUserService(TestCase):

    def test_create_user(self):
        """Test creating a user successfully."""
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "1234567890",
            "email": "john.doe@example.com",
            "role": "Tester",
            "department": "Quality",
            "access_level": "Admin"
        }
        response, status_code = create_user(user_data)
        self.assertEqual(status_code, 201)
        self.assertIn("John", response.json['first_name'])

    # def test_get_user_found(self):
    #     "Test retrieving a user that does exist."


    def test_get_user_not_found(self):
        """Test retrieving a user that does not exist."""
        response = get_user("nonexistingid")
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found", response.json['error'])





