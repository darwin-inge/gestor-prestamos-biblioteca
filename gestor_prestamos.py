prestamos = []


def mostrar_menu():
    """Dibuja la interfaz limpia del menú principal."""
    print("\n========================================")
    print("     GESTOR DE PRÉSTAMOS - BIBLIOTECA")
    print("========================================")
    print("1. Registrar nuevo préstamo")
    print("2. Ver libros prestados actualmente")
    print("3. Devolver un libro")
    print("4. Salir")
    print("========================================")


def registrar_prestamo():
    """Función para la Opción 1: Captura y almacena un nuevo préstamo."""
    print("\n--- REGISTRAR NUEVO PRÉSTAMO ---")
    libro = input("Ingrese el título del libro: ").strip()
    persona = input("Ingrese el nombre de la persona: ").strip()

    if libro and persona:
        # Creamos un formato de diccionario para guardarlo en la lista
        nuevo_registro = {"titulo": libro, "usuario": persona}
        prestamos.append(nuevo_registro)
        print(f"\n¡Préstamo registrado: '{libro}' entregado a {persona}!")
    else:
        print("\n[Error] El título del libro o el nombre no pueden estar vacíos.")


def ver_prestados():
    """Función para la Opción 2: Recorre y muestra los datos sin formato técnico."""
    print("\n--- LIBROS EN PRÉSTAMO ---")

    if not prestamos:
        print("Todos los libros están en la biblioteca.")
    else:
        # Bucle para recorrer la lista línea por línea sin mostrar corchetes ni comillas
        for registro in prestamos:
            print(f'* "{registro["titulo"]}" prestado a {registro["usuario"]}.')

    print("--------------------------")


def devolver_libro():
    """Función para la Opción 3: Busca, verifica y elimina un registro."""
    print("\n--- DEVOLVER UN LIBRO ---")
    libro_a_devolver = input("Ingrese el título del libro a devolver: ").strip()

    # Variable bandera (flag) para verificar si encontramos el libro
    encontrado = False

    # Recorremos la lista para buscar el libro de manera exacta
    for registro in prestamos:
        if registro["titulo"].lower() == libro_a_devolver.lower():
            # Si lo encuentra, usamos el método .remove() de las listas
            prestamos.remove(registro)
            print(f"\n¡El libro '{registro['titulo']}' ha sido devuelto con éxito!")
            encontrado = True
            break  # Rompemos el ciclo ya que el libro fue encontrado y devuelto

    if not encontrado:
        print(f"\nEl libro '{libro_a_devolver}' no se encuentra registrado como prestado.")


def ejecutar_sistema():
    """Bucle principal que controla el flujo del programa y valida las opciones."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            ver_prestados()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            print("\n¡Gracias por usar el Gestor de Préstamos! Que tenga un feliz día.")
            break  # Rompe el bucle while y cierra el programa de manera limpia
        else:
            print("\nOpción no válida. Por favor, intente de nuevo con números del 1 al 4.")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_sistema()
