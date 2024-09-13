from estudiante import Estudiante

def main():
    estudiante1 = Estudiante.crearEstudiante("Patrick", 19, "primer semestre")
    estudiante2 = Estudiante.crearEstudiante("Luis", 23, "segundo semestre")
    estudiante3 = Estudiante.crearEstudiante("Maria", 27, "quinto semestre")

    estudiantes = [estudiante1, estudiante2, estudiante3]

    for estudiante in estudiantes:
        estudiante.imprimirDatos()
        estudiante.matricular()
        estudiante.pagarPension()
        print()
    
    print(Estudiante.esMayorDeEdad(17))  
    print(Estudiante.esMayorDeEdad(18))  
    print(Estudiante.saludo())
    
    print(Estudiante.cantidadEstudiantes())

if __name__ == "__main__":
    main()
