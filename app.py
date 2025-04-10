import os
from flask import Flask
from routes.routes import routes_bp  # Import the Blueprint from routes.py
from config import DevelopmentConfig, ProductionConfig


# Initialize the Flask application
def create_app():

    environment = os.getenv('FLASK_ENV', 'development')

    if environment == 'production':
        config_class = ProductionConfig
    else:
        config_class = DevelopmentConfig

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    app.register_blueprint(routes_bp)

    return app


# Initialize the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
