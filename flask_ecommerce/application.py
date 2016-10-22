from importlib import import_module

from flask import Flask
from flask_ecommerce.modules import all_modules
from flask_ecommerce.services.database import sqlalchemy


def initialize_app(config_obj):
    app = Flask(__name__)

    for module in all_modules:
        import_module(module.import_name)
        app.register_blueprint(module)

    sqlalchemy.init_app(app)
    return app