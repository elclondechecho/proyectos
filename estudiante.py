class Estudiante:
    def __init__(self, nombre="", edad=0, semestre=""):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre

    def ingresarDatos(self):
        self.nombre = input("ingrese el nombre del estudiante: ")
        self.edad = int(input("ingrese la edad del estudiante: "))
        self.semestre = input("ingrese el semestre del estudiante: ")

    def imprimirDatos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"semestre: {self.semestre}")

    def matricular(self):
        print(f"{self.nombre} ha sido matriculado.")

    def pagarPension(self):
        print(f"{self.nombre} ha pagado la pensión.")
