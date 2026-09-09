from flask import current_app, jsonify
from Models.Curso import Curso

class cursoService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_CURSO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_CURSO WHERE CUR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Curso no encontrado"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_CURSO (CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('CUR_UUID'),
            data.get('CUR_NOMBRE'),
            data.get('CUR_CODIGO'),
            data.get('CUR_DURACION'),
            data.get('CUR_COSTO'),
            data.get('CUR_DESCRIPCION')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Curso agregado correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_CURSO SET CUR_NOMBRE=%s, CUR_CODIGO=%s, CUR_DURACION=%s, CUR_COSTO=%s, CUR_DESCRIPCION=%s 
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
        sql = "DELETE FROM T_CURSO WHERE CUR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
<<<<<<< HEAD
        return jsonify({"message": "Curso eliminado correctamente"})
=======
        return jsonify({"message": "Curso eliminado correctamente"})
>>>>>>> 1ec947b02867a883f1941a1d1892d20cd71fe47b
