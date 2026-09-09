from flask import request
from Services.evaluacionService import evaluacionService

class evaluacionController:

    @staticmethod
    def get_all():
        return evaluacionService.get_all()

    @staticmethod
    def get_by_id(id):
        return evaluacionService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return evaluacionService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return evaluacionService.update(id, data)

    @staticmethod
    def delete(id):
        return evaluacionService.delete(id)
