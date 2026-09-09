from flask import request
from Services.personaService import personaService

class PersonaController:

    @staticmethod
    def get_all():
        return personaService.get_all()

    @staticmethod
    def show():
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
        return personaService.delete(id)
