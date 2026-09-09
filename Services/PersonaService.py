from flask import current_app
from Models.Persona import Persona
from Services.dbUtils import serialize_rows, serialize_row
import uuid

class PersonaService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE

    @staticmethod
    def show():
        sql = "SELECT * FROM T_PERSONA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return serialize_rows(data)

    @staticmethod
    def get_all():
        return PersonaService.show()

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_PERSONA WHERE PER_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return serialize_row(data)

    @staticmethod
    def add(data):
        uuid_persona = str(uuid.uuid4())
        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_PERSONA (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOC)
                  VALUES (%s, %s, %s, %s, %s, %s) """
        pri_nombre = data.get("primer_nombre") or data.get("PER_PRI_NOMBRE") or ""
        seg_nombre = data.get("segundo_nombre") or data.get("PER_SEG_NOMBRE") or ""
        pri_apellido = data.get("primer_apellido") or data.get("PER_PRI_APELLIDO") or ""
        seg_apellido = data.get("segundo_apellido") or data.get("PER_SEG_APELLIDO") or ""
        documento = data.get("documento") or data.get("PER_DOC")

        if not pri_nombre or not pri_apellido or documento is None:
            raise ValueError("primer_nombre, primer_apellido y documento son requeridos")

        c.execute(sql, (uuid_persona, pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento))
        c.connection.commit()
        last_id = c.lastrowid
        c.close()

        return {
            "id": last_id,
            "PER_ID": last_id,
            "PER_UUID": uuid_persona,
            "PER_PRI_NOMBRE": pri_nombre,
            "PER_SEG_NOMBRE": seg_nombre,
            "PER_PRI_APELLIDO": pri_apellido,
            "PER_SEG_APELLIDO": seg_apellido,
            "PER_DOC": documento
        }

    @staticmethod
    def update(id, data):
        c = current_app.mysql.connection.cursor()
        sql = """ UPDATE T_PERSONA 
                  SET PER_PRI_NOMBRE = %s, PER_SEG_NOMBRE = %s, PER_PRI_APELLIDO = %s, PER_SEG_APELLIDO = %s, PER_DOC = %s
                  WHERE PER_ID = %s """
        pri_nombre = data.get("primer_nombre") or data.get("PER_PRI_NOMBRE")
        seg_nombre = data.get("segundo_nombre") or data.get("PER_SEG_NOMBRE") or ""
        pri_apellido = data.get("primer_apellido") or data.get("PER_PRI_APELLIDO")
        seg_apellido = data.get("segundo_apellido") or data.get("PER_SEG_APELLIDO") or ""
        documento = data.get("documento") or data.get("PER_DOC")

        c.execute(sql, (pri_nombre, seg_nombre, pri_apellido, seg_apellido, documento, id))
        c.connection.commit()
        affected = c.rowcount
        c.close()
        return {"affected": affected, "message": "Persona actualizada"}

    @staticmethod
    def delete(id):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_PERSONA WHERE PER_ID = %s"
        c.execute(sql, (id,))
        c.connection.commit()
        affected = c.rowcount
        c.close()
        return {"affected": affected, "message": "Persona eliminada"}


personaService = PersonaService
