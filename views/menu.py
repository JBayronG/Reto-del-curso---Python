from controllers.product_app import ProductApp  # Importa la clase ProductApp en lugar de 'product_app'

"Ejecutar el menú principal."
def gestionar_productos():
    productApp = ProductApp()  # Crear una instancia de la clase ProductApp
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")    
            precio_input = input("Precio: ").replace(',', '')  # Eliminar las comas y convertir el valor a float
            try:
                precio = float(precio_input)
            except ValueError:
                print("Por favor ingrese un precio válido.")
                continue  # Si el valor no es un número válido, continúa pidiendo la opción
            descripcion = input("Descripción: ")
            if descripcion == "":
                descripcion = None  # Si la descripción está vacía, asignar None
            productApp.agregar_producto(nombre, precio, descripcion)

        elif opcion == "2":
            productApp.ver_productos()

        elif opcion == "3":
            nombre = input("Nombre: ")
                 # Verificar si el producto existe
            if nombre not in productApp.products:
                print(f"El producto '{nombre}' no existe.")
                continue  # Si el producto no existe, seguir con el menú

            precio = input("Precio (opcional): ")
            descripcion = input("Descripción (opcional): ")

            if precio:
                precio = precio.replace(',', '')  # Eliminar comas
                try:
                    precio = float(precio)
                except ValueError:
                    print("Por favor ingrese un precio válido.")
                    continue  # Si el precio no es válido, sigue pidiendo la opció
            else:
                precio = None

            if descripcion == "":
               descripcion = None  # Asignar None si no se ingresa una descripción

            productApp.actualizar_producto(nombre, precio, descripcion)

        elif opcion == "4":
            nombre = input("Nombre: ")
            productApp.eliminar_producto(nombre)


        elif opcion == "5":
            break
        else:
            print("Opción inválida.")