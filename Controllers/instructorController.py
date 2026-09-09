<<<<<<< HEAD
=======
from flask import request
>>>>>>> 1ec947b02867a883f1941a1d1892d20cd71fe47b
from Services.instructorService import instructorService

class instructorController:

<<<<<<< HEAD
    def get_all():
        data = instructorService.get_all()
        return data

    def get_by_id(id):
        data = instructorService.get_by_id(id)
        return data

    def add():
        data = instructorService.add()
        return data

    def update(id):
        data = instructorService.update(id)
        return data

    def delete(id):
        data = instructorService.delete(id)
        return data
=======
    @staticmethod
    def get_all():
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
>>>>>>> 1ec947b02867a883f1941a1d1892d20cd71fe47b
