# blueprint  
from flask import Blueprint
from Controllers.aprendizController import aprendizController

persona_bp = Blueprint('persona_bp', __name__)

@persona_bp.route('/', methods=['GET'])
def home():
    aprendizController.show()

@persona_bp.route('/', methods=['POST'])
def add():
    return "agregar aprendiz"