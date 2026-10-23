from flask import Flask
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Connects the database extension to Flask
    db.init_app(app)   # connects Flask-SQLAlchemy to Flask application.
    migrate.init_app(app, db)  # connects Flask-Migrate so we can update the database structure safely.

    from app.models import Product  # imports the model, registering its table definition with SQLAlchemy. It ensures SQLAlchemy knows about our Product table.

    from app.routes import main

    app.register_blueprint(main)  # registers routes.

    return app
