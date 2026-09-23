import uuid
from flask import current_app, jsonify
from Models.Evaluacion import Evaluacion

class evaluacionService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM t_evaluacion"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM t_evaluacion WHERE EVA_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Evaluacion no encontrada"}), 404)

    @staticmethod
    def add(data):
        eva_uuid = data.get('EVA_UUID') or str(uuid.uuid4())
        eva_date = data.get('EVA_DATE') or data.get('EVA_FECHA')
        sql = """INSERT INTO t_evaluacion (EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_DATE) 
                 VALUES (%s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            eva_uuid,
            data.get('EVA_NOMBRE'),
            data.get('EVA_CODIGO'),
            data.get('EVA_PORCENTAJE'),
            eva_date
        ))
        current_app.mysql.connection.commit()
        last_id = c.lastrowid
        c.close()
        return jsonify({
            "message": "Evaluacion agregada correctamente",
            "EVA_ID": last_id,
            "EVA_UUID": eva_uuid
        }), 201

    @staticmethod
    def update(id, data):
        eva_date = data.get('EVA_DATE') or data.get('EVA_FECHA')
        sql = """UPDATE t_evaluacion SET EVA_NOMBRE=%s, EVA_CODIGO=%s, EVA_PORCENTAJE=%s, EVA_DATE=%s 
                 WHERE EVA_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('EVA_NOMBRE'),
            data.get('EVA_CODIGO'),
            data.get('EVA_PORCENTAJE'),
            eva_date,
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Evaluacion actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM t_evaluacion WHERE EVA_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Evaluacion eliminada correctamente"})
