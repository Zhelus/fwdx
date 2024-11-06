import json
from flask import Flask
from flask_testing import TestCase
from yourapplication.app import create_app  # Adjust the import according to your project structure
from yourapplication.models import db, User  # Assuming you're using SQLAlchemy

class TestUserRoutes(TestCase):

    def create_app(self):
        # Setup Flask application for testing
        app = create_app('testing')
        return app

    def setUp(self):
        # Setup the database, and other initial configurations
        db.create_all()
        # Optional: Add test data here

    def tearDown(self):
        # Teardown the database after tests
        db.session.remove()
        db.drop_all()

    def test_api_create_user(self):
        # Create a user through the API
        data = json.dumps({
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'john.doe@example.com',
            'role': 'Tester',
            'department': 'Quality Assurance',
            'access_level': 'Admin'
        })
        response = self.client.post('/users', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('John', response.json['first_name'])

    def test_api_get_user(self):
        # Assuming you have a method to add a user or have added a user in setUp
        user_id = 'some-user-id'  # Adjust based on your test setup
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_api_update_user(self):
        user_id = 'some-user-id'
        data = json.dumps({'first_name': 'Jane'})
        response = self.client.put(f'/users/{user_id}', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_api_delete_user(self):
        user_id = 'some-user-id'
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 204)

    def test_api_change_password(self):
        user_id = 'some-user-id'
        data = json.dumps({'newPassword': 'newSecurePassword123'})
        response = self.client.patch(f'/users/{user_id}/password', data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    import unittest
    unittest.main()
