#__init__.py
from flask import Flask
from .routes import APIRoutes
from flask_restful import Api

def crear_app():
    app = Flask(__name__)
    api = Api(app)  # Pasar la aplicación Flask al crear la instancia de Api

    routes = APIRoutes()
    routes.init_routes(api)

    return app
