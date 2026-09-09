from flask import current_app, jsonify
from Models.Imparte import Imparte

class imparteService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_IMPARTE"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_IMPARTE WHERE IMP_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Asignacion no encontrada"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_IMPARTE (IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID) 
                 VALUES (%s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('IMP_UUID'),
            data.get('IMP_ROL'),
            data.get('IMP_FECHA_ASIGNACION'),
            data.get('IMP_CUR_ID'),
            data.get('IMP_INS_ID')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Asignacion agregada correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_IMPARTE SET IMP_ROL=%s, IMP_FECHA_ASIGNACION=%s, IMP_CUR_ID=%s, IMP_INS_ID=%s 
                 WHERE IMP_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('IMP_ROL'),
            data.get('IMP_FECHA_ASIGNACION'),
            data.get('IMP_CUR_ID'),
            data.get('IMP_INS_ID'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Asignacion actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM T_IMPARTE WHERE IMP_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Asignacion eliminada correctamente"})
