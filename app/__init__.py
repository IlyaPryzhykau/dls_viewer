"""
App initialization module.

Creates the Flask application instance and imports routes to register them.
"""

from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Import and register routes (at the bottom to avoid circular imports)
from app import routes
