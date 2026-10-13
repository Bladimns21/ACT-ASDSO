from flask import Flask, jsonify, send_from_directory, request
from flask_mysqldb import MySQL
from Config import Config

from Routes.persona_bp import persona_bp
from Routes.aprendiz_bp import apr_bp
from Routes.instructor_bp import instructor_bp
from Routes.matricula_bp import matricula_bp
from Routes.curso_bp import curso_bp
from Routes.imparte_bp import imparte_bp
from Routes.evaluacion_bp import evaluacion_bp
from Routes.matEva_bp import mat_eva_bp

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

mysql = MySQL(app)
app.mysql = mysql

# Endpoints base
app.register_blueprint(persona_bp, url_prefix='/api/persona')
app.register_blueprint(apr_bp, url_prefix='/api/aprendiz')
app.register_blueprint(instructor_bp, url_prefix='/api/instructor')
app.register_blueprint(matricula_bp, url_prefix='/api/matricula')
app.register_blueprint(curso_bp, url_prefix='/api/curso')
app.register_blueprint(imparte_bp, url_prefix='/api/imparte')
app.register_blueprint(evaluacion_bp, url_prefix='/api/evaluacion')
app.register_blueprint(mat_eva_bp, url_prefix='/api/mat-eva')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,PATCH,OPTIONS'
    return response

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "online"}), 200

@app.route('/swagger.json', methods=['GET'])
def get_swagger_json():
    return send_from_directory('.', 'swagger.json')

@app.route('/docs', methods=['GET'])
@app.route('/docs/<path:path>', methods=['GET'])
def get_swagger_ui(path='index.html'):
    return send_from_directory('swagger-ui', path)


  #  app.run(debug=True, port=5000, host="0.0.0.0")

