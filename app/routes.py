#routes.py
from flask_restful import Resource

# Añadir los dos puntos al final de la clase
class HelloWorld(Resource):
    def get(self):
        # Las claves del diccionario deben estar entre comillas
        return { 'message': 'Hola mundo desde la API', 'status': 200 }

class APIRoutes:
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')
