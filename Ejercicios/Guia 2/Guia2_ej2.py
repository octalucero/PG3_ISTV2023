class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        if self.nota >= 6:
            print (f"El alumno {self.nombre} esta aprobado con", self.nota)
        else:
            print (f"El alumno {self.nombre} esta desaprobado con", self.nota)

nombre1 = (input("Ingrese nombre del alumno: "))
nota1 = float(input("Ingrese la nota del alumn: "))
alumno1 = Alumno(nombre1, nota1)
alumno1.mostrar()