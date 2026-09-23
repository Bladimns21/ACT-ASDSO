from flask import current_app, jsonify
from Models.Curso import Curso

class cursoService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM t_curso"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM t_curso WHERE CUR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Curso no encontrado"}), 404)

    @staticmethod
    def add(data):
        import uuid
        cur_uuid = data.get('CUR_UUID') or str(uuid.uuid4())
        sql = """INSERT INTO t_curso (CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            cur_uuid,
            data.get('CUR_NOMBRE'),
            data.get('CUR_CODIGO'),
            data.get('CUR_DURACION'),
            data.get('CUR_COSTO'),
            data.get('CUR_DESCRIPCION')
        ))
        current_app.mysql.connection.commit()
        last_id = c.lastrowid
        c.close()
        return jsonify({
            "message": "Curso agregado correctamente",
            "CUR_ID": last_id,
            "CUR_UUID": cur_uuid
        }), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE t_curso SET CUR_NOMBRE=%s, CUR_CODIGO=%s, CUR_DURACION=%s, CUR_COSTO=%s, CUR_DESCRIPCION=%s 
                 WHERE CUR_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('CUR_NOMBRE'),
            data.get('CUR_CODIGO'),
            data.get('CUR_DURACION'),
            data.get('CUR_COSTO'),
            data.get('CUR_DESCRIPCION'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Curso actualizado correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM t_curso WHERE CUR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Curso eliminado correctamente"})
