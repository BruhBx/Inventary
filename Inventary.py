inventario = []

while True:
    # Mostrar menú de opciones al usuario
    print("\n--- MENÚ DE GESTIÓN ---")
    print("1. Ingresar otro producto")
    print("2. Ver productos ingresados")
    print("3. Finalizar")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Bloque para solicitar datos al usuario
        nombre = input("Nombre del producto: ")
        
        # Validar que el precio sea un número (float)
        while True:
            try:
                precio = float(input("Precio: "))
                break
            except ValueError:
                print("Error: Ingrese un precio válido.")

        # Validar que la cantidad sea un número entero (int)
        while True:
            try:
                cantidad = int(input("Cantidad: "))
                break
            except ValueError:
                print("Error: Ingrese una cantidad entera.")

        # Calcular el costo total y guardar el producto en la lista
        costo_total = precio * cantidad
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "total": costo_total
        }
        inventario.append(producto)
        print(f"¡{nombre} agregado con éxito!")

    elif opcion == "2":
        # Bloque para mostrar los productos guardados en la lista
        if not inventario:
            print("\nNo hay productos registrados aún.")
        else:
            print("\n--- LISTA DE PRODUCTOS ---")
            for p in inventario:
                print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']} | Total: {p['total']}")

    elif opcion == "3":
        # Finalizar el programa
        print("Saliendo del programa... ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")

#_______________________________________________________________________________________
# Este programa gestiona un inventario interactivo permitiendo registrar productos, 
# validar tipos de datos numéricos y mostrar un resumen donde el costo total 
# se presenta como un número entero sin decimales.
