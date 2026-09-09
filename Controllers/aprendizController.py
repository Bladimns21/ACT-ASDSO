from flask import jsonify
from Services.aprendizService import aprendizService


class AprendizController:

    @staticmethod
    def show():
        data = aprendizService.show()
        return jsonify(data), 200


    @staticmethod
    def delete(idaprendiz):
        return aprendizService.delete(idaprendiz)



# cyflz16