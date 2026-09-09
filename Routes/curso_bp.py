from flask import Blueprint
from Controllers.cursoController import CursoController

curso_bp = Blueprint("curso_bp", __name__)

@curso_bp.route("/", methods=["GET"], strict_slashes=False)
def show():
    return CursoController.show()

@curso_bp.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_by_id(id):
    return CursoController.get_by_id(id)

@curso_bp.route("/", methods=["POST"], strict_slashes=False)
def add():
    return CursoController.add()

@curso_bp.route("/<int:id>", methods=["PUT", "PATCH"], strict_slashes=False)
def update(id):
    return CursoController.update(id)

@curso_bp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete(id):
    return CursoController.delete(id)
