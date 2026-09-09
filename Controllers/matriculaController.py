from flask import request
from Services.matriculaService import matriculaService

class matriculaController:

    @staticmethod
    def get_all():
        return matriculaService.get_all()

    @staticmethod
    def get_by_id(id):
        return matriculaService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return matriculaService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return matriculaService.update(id, data)

    @staticmethod
    def delete(id):
        return matriculaService.delete(id)
