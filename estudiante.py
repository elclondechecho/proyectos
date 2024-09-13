class Estudiante:
    def __new__(cls, *args, **kwargs):

        instance = super().__new__(cls)
        print(f"Creando una nueva instancia de {cls.__name__}")
        return instance

    def __init__(self, nombre="", edad=0, semestre=""):
        self._nombre = nombre
        self._edad = edad
        self._semestre = semestre
        print(f"Inicializando el estudiante: {self.nombre}")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            print("Edad debe ser positiva.")

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, valor):
        self._semestre = valor

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.edad = int(input("Ingrese la edad del estudiante: "))
        self.semestre = input("Ingrese el semestre del estudiante: ")

    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Semestre: {self.semestre}")

    def matricular(self):
        print(f"{self.nombre} ha sido matriculado.")

    def pagarPension(self):
        print(f"{self.nombre} ha pagado la pensión.")

    @classmethod
    def crearEstudiante(cls, nombre, edad, semestre):
        return cls(nombre, edad, semestre)

    @classmethod
    def cantidadEstudiantes(cls):

        return "Cantidad de estudiantes no disponible en esta implementación."

    @staticmethod
    def esMayorDeEdad(edad):
        return edad >= 18

    @staticmethod
    def saludo():
        return "¡Hola! Soy un estudiante."

    def __del__(self):
        print(f"Destruyendo la instancia de Estudiante: {self.nombre}")
