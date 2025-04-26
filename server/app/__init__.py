from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    
    # MongoDB connection
    client = MongoClient('mongodb://localhost:27017/')
    db = client['connectsphere']
    app.db = db  # Attach db to app for access in routes
    
    # Register routes
    from .routes import health
    app.register_blueprint(health.bp)
    
    return app