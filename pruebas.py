from estudiante import Estudiante

def main():
    print("Creando estudiantes...")
    estudiante1 = Estudiante("Patrick", 19, "primer semestre")
    estudiante2 = Estudiante("Luis", 23, "segundo semestre")
    estudiante3 = Estudiante("Maria", 27, "quinto semestre")

    estudiantes = [estudiante1, estudiante2, estudiante3]

    for estudiante in estudiantes:
        estudiante.imprimirDatos()
        estudiante.matricular()
        estudiante.pagarPension()
        print()

    print("Fin del programa. Los estudiantes serán destruidos.")

if __name__ == "__main__":
    main()
