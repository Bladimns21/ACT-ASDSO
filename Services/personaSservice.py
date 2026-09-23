import uuid
from flask import current_app, jsonify
from Models.Persona import Persona

class personaService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM t_persona"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM t_persona WHERE PER_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Persona no encontrada"}), 404)

    @staticmethod
    def add(data):
        per_uuid = data.get('PER_UUID') or str(uuid.uuid4())
        per_doc = data.get('PER_DOC') or data.get('PER_DOCUMENTO')
        sql = """INSERT INTO t_persona (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOC) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            per_uuid,
            data.get('PER_PRI_NOMBRE'),
            data.get('PER_SEG_NOMBRE'),
            data.get('PER_PRI_APELLIDO'),
            data.get('PER_SEG_APELLIDO'),
            per_doc
        ))
        current_app.mysql.connection.commit()
        last_id = c.lastrowid
        c.close()
        return jsonify({
            "message": "Persona agregada correctamente",
            "PER_ID": last_id,
            "PER_UUID": per_uuid
        }), 201

    @staticmethod
    def update(id, data):
        per_doc = data.get('PER_DOC') or data.get('PER_DOCUMENTO')
        sql = """UPDATE t_persona SET PER_PRI_NOMBRE=%s, PER_SEG_NOMBRE=%s, PER_PRI_APELLIDO=%s, PER_SEG_APELLIDO=%s, PER_DOC=%s 
                 WHERE PER_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('PER_PRI_NOMBRE'),
            data.get('PER_SEG_NOMBRE'),
            data.get('PER_PRI_APELLIDO'),
            data.get('PER_SEG_APELLIDO'),
            per_doc,
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Persona actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM t_persona WHERE PER_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Persona eliminada correctamente"})
