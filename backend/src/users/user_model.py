from mongoengine import Document, StringField, EmailField
from backend.src.database.db_connection import MongoDBConnector

class User(Document):
    """
    A User document schema definition for MongoDB.

    Attributes:
        first_name (StringField): The user's first name. Required.
        last_name (StringField): The user's last name. Required.
        phone_number (StringField): The user's phone number. Must be a string. Required.
        email (EmailField): The user's email address. Must be unique and is required.
        role (StringField): The user's role within the organization (e.g., 'Technician'). Required.
        department (StringField): The department where the user works. Required.
        access_level (StringField): The level of access the user has (e.g., 'Admin', 'User'). Required.

    The 'meta' dictionary specifies additional options for the MongoDB collection,
    such as the name of the collection ('users').

    Usage:
        - Used by services to create, update, delete, and retrieve user data.
        - Handles user validation at the database level.
    """
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    phone_number = StringField(required=True, max_length=20)
    email = EmailField(required=True, unique=True)
    role = StringField(required=True, max_length=50)
    department = StringField(required=True, max_length=50)
    access_level = StringField(required=True, max_length=50)

    meta = {'collection': 'users'}

