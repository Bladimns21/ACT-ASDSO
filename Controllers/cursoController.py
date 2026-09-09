from flask import request
from Services.cursoService import cursoService

class cursoController:

    @staticmethod
    def get_all():
        return cursoService.get_all()

    @staticmethod
    def get_by_id(id):
        return cursoService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return cursoService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return cursoService.update(id, data)

    @staticmethod
    def delete(id):
        return cursoService.delete(id)