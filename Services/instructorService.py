from flask import current_app, jsonify
from Models.Instructor import Instructor

class instructorService:
    @staticmethod
    def get_all():
        sql = "SELECT * FROM T_INSTRUCTOR"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        return jsonify(data)

    @staticmethod
    def get_by_id(id):
        sql = "SELECT * FROM T_INSTRUCTOR WHERE INS_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        data = c.fetchone()
        c.close()
        return jsonify(data) if data else (jsonify({"error": "Instructor no encontrado"}), 404)

    @staticmethod
    def add(data):
        sql = """INSERT INTO T_INSTRUCTOR (INS_UUID, INS_ESPECIALIDAD, INS_PER_ID) 
                 VALUES (%s, %s, %s)"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('INS_UUID'),
            data.get('INS_ESPECIALIDAD'),
            data.get('INS_PER_ID')
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Instructor agregado correctamente"}), 201

    @staticmethod
    def update(id, data):
        sql = """UPDATE T_INSTRUCTOR SET INS_ESPECIALIDAD=%s, INS_PER_ID=%s 
                 WHERE INS_ID=%s"""
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (
            data.get('INS_ESPECIALIDAD'),
            data.get('INS_PER_ID'),
            id
        ))
        current_app.mysql.connection.commit()
        c.close()
        return jsonify({"message": "Instructor actualizado correctamente"})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM T_INSTRUCTOR WHERE INS_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        c.close()
<<<<<<< HEAD
        return jsonify({"message": "Instructor eliminado correctamente"})
=======
        return jsonify({"message": "Instructor eliminado correctamente"})
>>>>>>> 1ec947b02867a883f1941a1d1892d20cd71fe47b
