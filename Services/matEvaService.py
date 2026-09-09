from flask import current_app, jsonify
from Models.MatEva import MatEva

class matEvaService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_MAT_EVA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_MAT_EVA WHERE MATE_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Nota de evaluacion no encontrada"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_MAT_EVA (MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID) 
                 VALUES (%s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('MATE_UUID'),
            data.get('MATE_NOTA'),
            data.get('MATE_EVA_ID'),
            data.get('MATE_MAT_ID')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Nota de evaluacion registrada correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_MAT_EVA SET MATE_NOTA=%s, MATE_EVA_ID=%s, MATE_MAT_ID=%s 
                 WHERE MATE_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('MATE_NOTA'),
            data.get('MATE_EVA_ID'),
            data.get('MATE_MAT_ID'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Nota de evaluacion actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM T_MAT_EVA WHERE MATE_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Nota de evaluacion eliminada correctamente"})
