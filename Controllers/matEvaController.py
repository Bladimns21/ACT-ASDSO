from flask import request
from Services.matEvaService import matEvaService

class matEvaController:

    @staticmethod
    def get_all():
        return matEvaService.get_all()

    @staticmethod
    def get_by_id(id):
        return matEvaService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return matEvaService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return matEvaService.update(id, data)

    @staticmethod
    def delete(id):
        return matEvaService.delete(id)
