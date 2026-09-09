from flask import current_app, jsonify
from Models.Evaluacion import Evaluacion

class evaluacionService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_EVALAUCION"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_EVALAUCION WHERE EVA_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Evaluacion no encontrada"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_EVALAUCION (EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA) 
                 VALUES (%s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('EVA_UUID'),
            data.get('EVA_NOMBRE'),
            data.get('EVA_CODIGO'),
            data.get('EVA_PORCENTAJE'),
            data.get('EVA_FECHA')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Evaluacion agregada correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_EVALAUCION SET EVA_NOMBRE=%s, EVA_CODIGO=%s, EVA_PORCENTAJE=%s, EVA_FECHA=%s 
                 WHERE EVA_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('EVA_NOMBRE'),
            data.get('EVA_CODIGO'),
            data.get('EVA_PORCENTAJE'),
            data.get('EVA_FECHA'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Evaluacion actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM T_EVALAUCION WHERE EVA_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Evaluacion eliminada correctamente"})
