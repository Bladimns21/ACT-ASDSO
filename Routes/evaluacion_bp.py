from flask import Blueprint
from Controllers.evaluacionController import EvaluacionController

evaluacion_bp = Blueprint("evaluacion_bp", __name__)

@evaluacion_bp.route("/", methods=["GET"], strict_slashes=False)
def show():
    return EvaluacionController.show()

@evaluacion_bp.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_by_id(id):
    return EvaluacionController.get_by_id(id)

@evaluacion_bp.route("/", methods=["POST"], strict_slashes=False)
def add():
    return EvaluacionController.add()

@evaluacion_bp.route("/<int:id>", methods=["PUT", "PATCH"], strict_slashes=False)
def update(id):
    return EvaluacionController.update(id)

@evaluacion_bp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete(id):
    return EvaluacionController.delete(id)
