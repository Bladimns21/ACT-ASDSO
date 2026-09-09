from flask import current_app
from Models.Aprendiz import Aprendiz

class aprendizService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add():
        pass

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_APRENDIZ"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [  Aprendiz(x[0],x[1],x[2],x[3]).to_dict() for x in data ]
        c.close()
        return data
