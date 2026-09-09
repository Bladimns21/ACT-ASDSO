from flask import Blueprint
from Controllers.materiaEvaluaController import materiaEvaluaController

materia_evalua_bp = Blueprint("materia_evalua_bp", __name__)

@materia_evalua_bp.route("/", methods=["GET"], strict_slashes=False)
def show():
    return materiaEvaluaController.show()

@materia_evalua_bp.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_by_id(id):
    return materiaEvaluaController.get_by_id(id)

@materia_evalua_bp.route("/", methods=["POST"], strict_slashes=False)
def add():
    return materiaEvaluaController.add()

@materia_evalua_bp.route("/<int:id>", methods=["PUT", "PATCH"], strict_slashes=False)
def update(id):
    return materiaEvaluaController.update(id)

@materia_evalua_bp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete(id):
    return materiaEvaluaController.delete(id)


mat_eva_bp = materia_evalua_bp
