from estudiante import Estudiante

def main():

    estudiantes = [
        Estudiante("patrick", 19, "primer semestre"),
        Estudiante("Luis", 23, "segundo semestre"),
        Estudiante("Maria", 27, "quinto semestre")
    ]

    for estudiante in estudiantes:
        estudiante.imprimirDatos()
        estudiante.matricular()
        estudiante.pagarPension()
        print()

if __name__ == "__main__":
    main()
