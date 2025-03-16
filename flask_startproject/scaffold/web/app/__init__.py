import os
from flask import Flask
from .extensions import register_extensions
from .config.development import DevelopmentConfig
from .config.production import ProductionConfig

def create_app():
    app = Flask(__name__)
    config_name = os.getenv("FLASK_ENV", "development")
    
    if config_name == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    register_extensions(app)

    return app