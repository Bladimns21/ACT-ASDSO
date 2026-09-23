from flask import current_app, jsonify
from Models.Matricula import Matricula

class matriculaService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM t_matricula"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM t_matricula WHERE MAT_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Matricula no encontrada"}), 404)

    @staticmethod
    def add(data):
        import uuid
        mat_uuid = data.get('MAT_UUID') or str(uuid.uuid4())
        fecha = data.get('MAT_FECHA_INSCRIPCION') or data.get('MAT_FECHA_INCRIPCION')
        c = current_app.mysql.connection.cursor()
        try:
            sql = """INSERT INTO t_matricula (MAT_UUID, MAT_ESTADO, MAT_FECHA_INCRIPCION, MAT_APR_ID, MAT_CUR_ID) 
                     VALUES (%s, %s, %s, %s, %s)"""
            c.execute(sql, (mat_uuid, data.get('MAT_ESTADO'), fecha, data.get('MAT_APR_ID'), data.get('MAT_CUR_ID')))
        except Exception:
            sql = """INSERT INTO t_matricula (MAT_UUID, MAT_ESTADO, MAT_FECHA_INSCRIPCION, MAT_APR_ID, MAT_CUR_ID) 
                     VALUES (%s, %s, %s, %s, %s)"""
            c.execute(sql, (mat_uuid, data.get('MAT_ESTADO'), fecha, data.get('MAT_APR_ID'), data.get('MAT_CUR_ID')))
        current_app.mysql.connection.commit()
        last_id = c.lastrowid
        c.close()
        return jsonify({
            "message": "Matricula agregada correctamente",
            "MAT_ID": last_id,
            "MAT_UUID": mat_uuid
        }), 201

    @staticmethod
    def update(id, data):
        fecha = data.get('MAT_FECHA_INSCRIPCION') or data.get('MAT_FECHA_INCRIPCION')
        c = current_app.mysql.connection.cursor()
        try:
            sql = """UPDATE t_matricula SET MAT_ESTADO=%s, MAT_FECHA_INCRIPCION=%s, MAT_APR_ID=%s, MAT_CUR_ID=%s 
                     WHERE MAT_ID=%s"""
            c.execute(sql, (data.get('MAT_ESTADO'), fecha, data.get('MAT_APR_ID'), data.get('MAT_CUR_ID'), id))
        except Exception:
            sql = """UPDATE t_matricula SET MAT_ESTADO=%s, MAT_FECHA_INSCRIPCION=%s, MAT_APR_ID=%s, MAT_CUR_ID=%s 
                     WHERE MAT_ID=%s"""
            c.execute(sql, (data.get('MAT_ESTADO'), fecha, data.get('MAT_APR_ID'), data.get('MAT_CUR_ID'), id))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Matricula actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM t_matricula WHERE MAT_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Matricula eliminada correctamente"})
