from flask import request
from Services.imparteService import imparteService

class imparteController:

    @staticmethod
    def get_all():
        return imparteService.get_all()

    @staticmethod
    def get_by_id(id):
        return imparteService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return imparteService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return imparteService.update(id, data)

    @staticmethod
    def delete(id):
        return imparteService.delete(id)
