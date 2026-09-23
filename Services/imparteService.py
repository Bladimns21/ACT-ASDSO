from flask import current_app, jsonify
from Models.Imparte import Imparte

class imparteService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM t_imparte"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM t_imparte WHERE IMP_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Asignacion no encontrada"}), 404)

    @staticmethod
    def add(data):
        import uuid
        imp_uuid = data.get('IMP_UUID') or str(uuid.uuid4())
        sql = """INSERT INTO t_imparte (IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID) 
                 VALUES (%s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            imp_uuid,
            data.get('IMP_ROL'),
            data.get('IMP_FECHA_ASIGNACION'),
            data.get('IMP_CUR_ID'),
            data.get('IMP_INS_ID')
        ))
        current_app.mysql.connection.commit()
        last_id = c.lastrowid
        c.close()
        return jsonify({
            "message": "Asignacion agregada correctamente",
            "IMP_ID": last_id,
            "IMP_UUID": imp_uuid
        }), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE t_imparte SET IMP_ROL=%s, IMP_FECHA_ASIGNACION=%s, IMP_CUR_ID=%s, IMP_INS_ID=%s 
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
        sql = "DELETE FROM t_imparte WHERE IMP_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Asignacion eliminada correctamente"})
