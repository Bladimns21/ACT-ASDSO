from flask import current_app, jsonify
from Models.Persona import Persona

class personaService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_PERSONA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_PERSONA WHERE PER_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Persona no encontrada"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_PERSONA (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOCUMENTO) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('PER_UUID'),
            data.get('PER_PRI_NOMBRE'),
            data.get('PER_SEG_NOMBRE'),
            data.get('PER_PRI_APELLIDO'),
            data.get('PER_SEG_APELLIDO'),
            data.get('PER_DOCUMENTO')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Persona agregada correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_PERSONA SET PER_PRI_NOMBRE=%s, PER_SEG_NOMBRE=%s, PER_PRI_APELLIDO=%s, PER_SEG_APELLIDO=%s, PER_DOCUMENTO=%s 
                 WHERE PER_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('PER_PRI_NOMBRE'),
            data.get('PER_SEG_NOMBRE'),
            data.get('PER_PRI_APELLIDO'),
            data.get('PER_SEG_APELLIDO'),
            data.get('PER_DOCUMENTO'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Persona actualizada correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM T_PERSONA WHERE PER_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Persona eliminada correctamente"})
