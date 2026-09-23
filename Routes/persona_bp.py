# blueprint  
from flask import Blueprint
from Controllers.personaController import PersonaController

persona_bp = Blueprint('persona_bp', __name__)

@persona_bp.route('/', methods=['GET'], strict_slashes=False)
def home():
    return PersonaController.get_all()

@persona_bp.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_by_id(id):
    return PersonaController.get_by_id(id)

@persona_bp.route('/', methods=['POST'], strict_slashes=False)
def add():
    return PersonaController.add()

@persona_bp.route('/<int:id>', methods=['PUT', 'PATCH'], strict_slashes=False)
def update(id):
    return PersonaController.update(id)

@persona_bp.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete(id):
    return PersonaController.delete(id)