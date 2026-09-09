from flask import Blueprint
from Controllers.imparteController import ImparteController

imparte_bp = Blueprint("imparte_bp", __name__)

@imparte_bp.route("/", methods=["GET"], strict_slashes=False)
def show():
    return ImparteController.show()

@imparte_bp.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_by_id(id):
    return ImparteController.get_by_id(id)

@imparte_bp.route("/", methods=["POST"], strict_slashes=False)
def add():
    return ImparteController.add()

@imparte_bp.route("/<int:id>", methods=["PUT", "PATCH"], strict_slashes=False)
def update(id):
    return ImparteController.update(id)

@imparte_bp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete(id):
    return ImparteController.delete(id)
