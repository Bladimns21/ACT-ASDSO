from flask import current_app
from Models.MatEva import MatEva
from Services.dbUtils import serialize_rows, serialize_row
import uuid

class materia_evaluaService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE

    @staticmethod
    def show():
        sql = "SELECT * FROM T_MAT_EVA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return serialize_rows(data)

    @staticmethod
    def get_all():
        return materia_evaluaService.show()

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_MAT_EVA WHERE MATE_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return serialize_row(data)

    @staticmethod
    def add(data):
        uuid_mat_eva = str(uuid.uuid4())
        eva_id = data.get("eva_id") or data.get("MATE_EVA_ID")
        mat_id = data.get("mat_id") or data.get("MATE_MAT_ID")
        nota = data.get("nota") if data.get("nota") is not None else data.get("MATE_NOTA")

        if eva_id is None or mat_id is None:
            raise ValueError("eva_id y mat_id son requeridos")

        c = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_MAT_EVA (MATE_UUID, MATE_EVA_ID, MATE_MAT_ID, MATE_NOTA) 
                  VALUES (%s, %s, %s, %s) """
        c.execute(sql, (uuid_mat_eva, eva_id, mat_id, nota))
        c.connection.commit()
        last_id = c.lastrowid
        c.close()

        return {
            "id": last_id,
            "MATE_ID": last_id,
            "MATE_UUID": uuid_mat_eva,
            "MATE_EVA_ID": eva_id,
            "MATE_MAT_ID": mat_id,
            "MATE_NOTA": float(nota) if nota is not None else None
        }

    @staticmethod
    def update(id, data):
        c = current_app.mysql.connection.cursor()
        sql = """ UPDATE T_MAT_EVA 
                  SET MATE_EVA_ID = %s, MATE_MAT_ID = %s, MATE_NOTA = %s 
                  WHERE MATE_ID = %s """
        eva_id = data.get("eva_id") or data.get("MATE_EVA_ID")
        mat_id = data.get("mat_id") or data.get("MATE_MAT_ID")
        nota = data.get("nota") if data.get("nota") is not None else data.get("MATE_NOTA")

        c.execute(sql, (eva_id, mat_id, nota, id))
        c.connection.commit()
        affected = c.rowcount
        c.close()
        return {"affected": affected, "message": "Calificación materia_evalua actualizada"}

    @staticmethod
    def delete(id):
        c = current_app.mysql.connection.cursor()
        sql = "DELETE FROM T_MAT_EVA WHERE MATE_ID = %s"
        c.execute(sql, (id,))
        c.connection.commit()
        affected = c.rowcount
        c.close()
        return {"affected": affected, "message": "Calificación materia_evalua eliminada"}


matEvaService = materia_evaluaService
MateriaEvaluaService = materia_evaluaService
