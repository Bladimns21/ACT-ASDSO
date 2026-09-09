from flask import request
from Services.personaService import personaService

class personaController:

    @staticmethod
    def get_all():
        return personaService.get_all()

    @staticmethod
    def get_by_id(id):
        return personaService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return personaService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return personaService.update(id, data)

    @staticmethod
    def delete(id):
<<<<<<< HEAD
        return personaService.delete(id)
=======
        return personaService.delete(id)
>>>>>>> 1ec947b02867a883f1941a1d1892d20cd71fe47b
