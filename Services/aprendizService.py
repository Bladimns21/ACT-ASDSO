import uuid
from flask import current_app
from Models.Aprendiz import Aprendiz

class aprendizService:

    @staticmethod
    def show():
        sql = "SELECT APR_ID, APR_UUID, APR_FECHA_NAC, APR_PER_ID FROM t_aprendiz"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        result = []
        for x in data:
            apr_id = x['APR_ID'] if isinstance(x, dict) else x[0]
            apr_uuid = x['APR_UUID'] if isinstance(x, dict) else x[1]
            fecha_val = x['APR_FECHA_NAC'] if isinstance(x, dict) else x[2]
            fecha = str(fecha_val) if hasattr(fecha_val, 'isoformat') else fecha_val
            per_id = x['APR_PER_ID'] if isinstance(x, dict) else x[3]
            result.append(Aprendiz(apr_id, apr_uuid, fecha, per_id).to_dict())
        c.close()
        return result

    @staticmethod
    def get_by_id(id):
        sql = "SELECT APR_ID, APR_UUID, APR_FECHA_NAC, APR_PER_ID FROM t_aprendiz WHERE APR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        x = c.fetchone()
        c.close()
        if not x:
            return None
        apr_id = x['APR_ID'] if isinstance(x, dict) else x[0]
        apr_uuid = x['APR_UUID'] if isinstance(x, dict) else x[1]
        fecha_val = x['APR_FECHA_NAC'] if isinstance(x, dict) else x[2]
        fecha = str(fecha_val) if hasattr(fecha_val, 'isoformat') else fecha_val
        per_id = x['APR_PER_ID'] if isinstance(x, dict) else x[3]
        return Aprendiz(apr_id, apr_uuid, fecha, per_id).to_dict()

    @staticmethod
    def add(data):
        apr_uuid = data.get('APR_UUID') or str(uuid.uuid4())
        fecha_nac = data.get('APR_FECHA_NAC') or data.get('fecha_nac')
        per_id = data.get('APR_PER_ID') or data.get('per_id')

        if not fecha_nac or not per_id:
            return {"error": "APR_FECHA_NAC y APR_PER_ID son obligatorios"}, 400

        c = current_app.mysql.connection.cursor()
        sql = """
            INSERT INTO t_aprendiz (APR_UUID, APR_FECHA_NAC, APR_PER_ID)
            VALUES (%s, %s, %s)
        """
        c.execute(sql, (apr_uuid, fecha_nac, per_id))
        current_app.mysql.connection.commit()
        last_id = c.lastrowid
        c.close()
        return {
            "message": "Aprendiz agregado correctamente",
            "APR_ID": last_id,
            "APR_UUID": apr_uuid
        }, 201

    @staticmethod
    def update(id, data):
        fecha_nac = data.get('APR_FECHA_NAC') or data.get('fecha_nac')
        per_id = data.get('APR_PER_ID') or data.get('per_id')

        if not fecha_nac or not per_id:
            return {"error": "APR_FECHA_NAC y APR_PER_ID son requeridos para actualizar"}, 400

        c = current_app.mysql.connection.cursor()
        sql = """
            UPDATE t_aprendiz 
            SET APR_FECHA_NAC = %s, APR_PER_ID = %s 
            WHERE APR_ID = %s
        """
        c.execute(sql, (fecha_nac, per_id, id))
        current_app.mysql.connection.commit()
        affected = c.rowcount
        c.close()
        if affected == 0:
            return {"error": "Aprendiz no encontrado o sin cambios"}, 404
        return {"message": "Aprendiz actualizado correctamente"}, 200

    @staticmethod
    def delete(id):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM t_aprendiz WHERE APR_ID = %s"
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        affected = c.rowcount
        c.close()
        if affected == 0:
            return {"error": "Aprendiz no encontrado"}, 404
        return {"message": "Aprendiz eliminado correctamente"}, 200
