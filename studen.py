from database import Data

data = Data()

class Functionality:

    def __init__(self):

        while True:
            self.menu()
            option = int(input("Ingrese opcion: "))

            if option == 1: self.add_student()
            elif option == 2: self.update_student()
            elif option == 3: self.delete_student()
            elif option == 4: self.get_student()
            elif option == 5: self.display_student()
            elif option == 6: self.search_student()

    def menu(self):
        print("1 - Agregar estudiante")
        print("2 - Actualizar estudiante")
        print("3 - Eliminar estudiante")
        print("4 - Obtener estudiante")
        print("5 - Mostrar estudiantes")
        print("6 - Buscar estudiantes")


    def add_student(self):
        name = input("Digite nombre: ")
        address = input("Digite direccion: ")
        age = int(input("Digite edad: "))
        
        try:
            data.add_student(name,address,age)
            print("Estudiante ingresado")
        except:
            print("Surgio algun error")
        

    def update_student(self):
        self.display_student()
        id = input("Digite el id: ")
        name = input("Digite nombre: ")
        address = input("Digite direccion: ")
        age = int(input("Digite edad: "))

        try:
            data.update_student(id,name,address,age)
            print("Estudiante actualizado")
        except:
            print("Surgio algun error")


    def delete_student(self):
        self.display_student()
        id = input("Digite el id: ")

        try:
            student = data.delete_student(id)
            print("Estudiante eliminado - ",id)
        except:
            print("Surgio algun error")

    def get_student(self):
        id = input("Digite el id: ")
        student = data.get_student(id)
        print("Datos del estudiante: ")
        print(student)

    def display_student(self):
        students = data.display_student()
        print("Lista de estudiantes:\n=======================================")
        for student in students:
            print(student)

    def search_student(self):
        name = input("Buscar: ")

        students = data.search_student(name)
        print("Lista de estudiantes por nombre:\n=======================================")
        for student in students:
            print(student)


if __name__ == '__main__':
    Functionality()
    