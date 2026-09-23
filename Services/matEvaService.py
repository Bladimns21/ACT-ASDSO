from flask import current_app, jsonify
from Models.MatEva import MatEva

class matEvaService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM t_mat_eva"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM t_mat_eva WHERE MATE_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Nota de evaluacion no encontrada"}), 404)

    @staticmethod
    def add(data):
        import uuid
        mate_uuid = data.get('MATE_UUID') or str(uuid.uuid4())
        sql = """INSERT INTO t_mat_eva (MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID) 
                 VALUES (%s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            mate_uuid,
            data.get('MATE_NOTA'),
            data.get('MATE_EVA_ID'),
            data.get('MATE_MAT_ID')
        ))
        current_app.mysql.connection.commit()
        last_id = c.lastrowid
        c.close()
        return jsonify({
            "message": "Nota de evaluacion registrada correctamente",
            "MATE_ID": last_id,
            "MATE_UUID": mate_uuid
        }), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE t_mat_eva SET MATE_NOTA=%s, MATE_EVA_ID=%s, MATE_MAT_ID=%s 
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
        sql = "DELETE FROM t_mat_eva WHERE MATE_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Nota de evaluacion eliminada correctamente"})
