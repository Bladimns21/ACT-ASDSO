from flask import Blueprint
from Controllers.aprendizController import AprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'], strict_slashes=False)
def home():
    return AprendizController.show()

@apr_bp.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_by_id(id):
    return AprendizController.get_by_id(id)

@apr_bp.route('/', methods=['POST'], strict_slashes=False)
def add():
    return AprendizController.add()

@apr_bp.route('/<int:id>', methods=['PUT', 'PATCH'], strict_slashes=False)
def update(id):
    return AprendizController.update(id)

@apr_bp.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete(id):
    return AprendizController.delete(id)