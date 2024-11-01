import os

"""
Definitions for common paths to configuration files.

Last edited by: Harrison Leath
Date: 10/30/24
"""

# ROOT_DIR assumes your config.env file is located directly under the backend folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # path to project root
ENV_DIR = os.path.join(ROOT_DIR, 'config.env')