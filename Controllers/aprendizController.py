from flask import jsonify, request
from Services.aprendizService import aprendizService

class AprendizController:

    @staticmethod
    def show():
        data = aprendizService.show()
        return jsonify(data), 200

    @staticmethod
    def get_by_id(id):
        data = aprendizService.get_by_id(id)
        if not data:
            return jsonify({"error": "Aprendiz no encontrado"}), 404
        return jsonify(data), 200

    @staticmethod
    def add():
        data = request.get_json() or {}
        resp, status = aprendizService.add(data)
        return jsonify(resp), status

    @staticmethod
    def update(id):
        data = request.get_json() or {}
        resp, status = aprendizService.update(id, data)
        return jsonify(resp), status

    @staticmethod
    def delete(id):
        resp, status = aprendizService.delete(id)
        return jsonify(resp), status