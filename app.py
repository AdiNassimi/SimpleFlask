from flask import Flask
from routes.routes import routes_bp  # Import the Blueprint from routes.py

app = Flask(__name__)

# db.init_app(app)
# with app.app_context():
#     db.create_all()

app.register_blueprint(routes_bp)  # Register Blueprint

if __name__ == '__main__':

    app.run(debug=True)
