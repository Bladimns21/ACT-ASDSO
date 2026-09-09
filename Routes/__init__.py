from .aprendiz_bp import apr_bp
# from .persona_bp import persona_bp


def loadRoutes(app):

    app.register_blueprint(apr_bp, url_prefix='/aprendices')
    # app.register_blueprint(persona_bp, url_prefix='/personas')