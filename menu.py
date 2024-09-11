from estudiante import Estudiante

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ingresar datos")
    print("2. Imprimir datos")
    print("3. Matricular")
    print("4. Pagar pensión")
    print("5. Salir")

def opciones():
    estudiante = Estudiante() 

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            estudiante.ingresarDatos()
        elif opcion == "2":
            estudiante.imprimirDatos()
        elif opcion == "3":
            estudiante.matricular()
        elif opcion == "4":
            estudiante.pagarPension()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción invalida. Intente de nuevo.")

if __name__ == "__main__":
    opciones()
