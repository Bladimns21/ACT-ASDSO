from flask import Blueprint
from Controllers.matriculaController import MatriculaController

matricula_bp = Blueprint("matricula_bp", __name__)

@matricula_bp.route("/", methods=["GET"], strict_slashes=False)
def show():
    return MatriculaController.show()

@matricula_bp.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_by_id(id):
    return MatriculaController.get_by_id(id)

@matricula_bp.route("/", methods=["POST"], strict_slashes=False)
def add():
    return MatriculaController.add()

@matricula_bp.route("/<int:id>", methods=["PUT", "PATCH"], strict_slashes=False)
def update(id):
    return MatriculaController.update(id)

@matricula_bp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete(id):
    return MatriculaController.delete(id)
