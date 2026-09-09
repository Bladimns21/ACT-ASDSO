from flask import Blueprint
from Controllers.instructorController import InstructorController

instructor_bp = Blueprint("instructor_bp", __name__)

@instructor_bp.route("/", methods=["GET"], strict_slashes=False)
def show():
    return InstructorController.show()

@instructor_bp.route("/<int:id>", methods=["GET"], strict_slashes=False)
def get_by_id(id):
    return InstructorController.get_by_id(id)

@instructor_bp.route("/", methods=["POST"], strict_slashes=False)
def add():
    return InstructorController.add()

@instructor_bp.route("/<int:id>", methods=["PUT", "PATCH"], strict_slashes=False)
def update(id):
    return InstructorController.update(id)

@instructor_bp.route("/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete(id):
    return InstructorController.delete(id)
