from flask import request
from Services.instructorService import instructorService

class InstructorController:

    @staticmethod
    def get_all():
        return instructorService.get_all()

    @staticmethod
    def show():
        return instructorService.get_all()

    @staticmethod
    def get_by_id(id):
        return instructorService.get_by_id(id)

    @staticmethod
    def add():
        data = request.get_json() or {}
        return instructorService.add(data)

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        return instructorService.update(id, data)

    @staticmethod
    def delete(id):
        return instructorService.delete(id)


instructorController = InstructorController
