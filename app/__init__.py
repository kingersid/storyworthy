from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    # Register the blueprint
    from routes.entry_routes import entry_routes
    app.register_blueprint(entry_routes)

    return app