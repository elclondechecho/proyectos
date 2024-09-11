from estudiante import Estudiante


def main():
    estudiante = Estudiante(nombre="sergio", edad=18, semestre="primer semestre")
    
    print("Datos iniciales del estudiante:")
    estudiante.imprimirDatos()
    
    estudiante.ingresarDatos()
    
    print("Datos después de ingresar nuevos datos:")
    estudiante.imprimirDatos()
    
    estudiante.matricular()
    estudiante.pagarPension()

if __name__ == "__main__":
    main()

