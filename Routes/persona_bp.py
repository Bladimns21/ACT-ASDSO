# blueprint  
from flask import Blueprint
from Controllers.personaController import PersonaController

persona_bp = Blueprint('persona_bp', __name__)

@persona_bp.route('/', methods=['GET'])
def home():
    return PersonaController.get_all()

@persona_bp.route('/', methods=['POST'])
def add():
    return "agregar aprendiz"