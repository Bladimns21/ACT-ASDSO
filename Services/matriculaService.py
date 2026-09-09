from flask import current_app, jsonify
from Models.Matricula import Matricula

class matriculaService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_MATRICULA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_MATRICULA WHERE MAT_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Matricula no encontrada"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_MATRICULA (MAT_UUID, MAT_ESTADO, MAT_FECHA_INSCRIPCION, MAT_APR_ID, MAT_CUR_ID) 
                 VALUES (%s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('MAT_UUID'),
            data.get('MAT_ESTADO'),
            data.get('MAT_FECHA_INSCRIPCION'),
            data.get('MAT_APR_ID'),
            data.get('MAT_CUR_ID')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Matricula agregada correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_MATRICULA SET MAT_ESTADO=%s, MAT_FECHA_INSCRIPCION=%s, MAT_APR_ID=%s, MAT_CUR_ID=%s 
                 WHERE MAT_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('MAT_ESTADO'),
            data.get('MAT_FECHA_INSCRIPCION'),
            data.get('MAT_APR_ID'),
            data.get('MAT_CUR_ID'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Matricula actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM T_MATRICULA WHERE MAT_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Matricula eliminada correctamente"})
