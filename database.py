from connection import *

class Data(Connection):

    def add_student(self, name, address, age):
        cnx = self.Connect()
        cursor = cnx.cursor()
        query = "INSERT INTO students (name, address, age) VALUES (%s,%s,%s)"
        cursor.execute(query, (name,address,age))
        cnx.commit()
        self.CloseConnection(cnx)
    
    def display_student(self):
        cnx = self.Connect()
        cursor = cnx.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        Lista = cursor.fetchall()
        self.CloseConnection(cnx)
        return Lista
    
    def get_student(self, id):
        cnx = self.Connect()
        cursor = cnx.cursor()
        query = "SELECT * FROM students WHERE id=%s"
        cursor.execute(query, (id))
        Lista = cursor.fetchall()
        self.CloseConnection(cnx)
        return Lista[0]

    def update_student(self, id, name, address, age):
        cnx = self.Connect()
        cursor = cnx.cursor()
        query = "UPDATE students SET name=%s, address=%s, age=%s WHERE id=%s"
        cursor.execute(query, (name,address,age,id))
        cnx.commit()
        self.CloseConnection(cnx)
    
    def delete_student(self, id):
        cnx = self.Connect()
        cursor = cnx.cursor()
        query = "DELETE FROM students WHERE id=%s"
        cursor.execute(query, (id))
        cnx.commit()
        self.CloseConnection(cnx)
    
    def search_student(self, name):
        cnx = self.Connect()
        cursor = cnx.cursor()
        query = "SELECT * FROM students WHERE name LIKE '{}%'".format(name)
        cursor.execute(query)
        Lista = cursor.fetchall()
        self.CloseConnection(cnx)
        return Lista