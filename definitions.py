import os
import platform

"""
Definitions for common paths to configuration files.
"""

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # path to project root
ENV_DIR = os.path.join(ROOT_DIR, 'config.env')