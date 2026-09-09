from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def home():
    return aprendizController.show()

@apr_bp.route('/', methods=['POST'])
def add():
    return "agregar aprendiz"


@apr_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return "borrar aprendiz"

@apr_bp.route('/<int:id>', methods=['GET'])
def searchByID(id):
    return f" aprendiz {id}"