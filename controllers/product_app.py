"Clase para gestionar la aplicación de productos."
# En controllers/product_app.py
from models.Product import Product  # importar la clase Product

class ProductApp:
    def __init__(self):
        self.products = {}

    def agregar_producto(self, nombre: str, precio: float, descripcion: str):
        if nombre in self.products:
            print(f"El producto '{nombre}' ya existe.")
        else:
            self.products[nombre] = Product(nombre, precio, descripcion)
            print(f"Producto '{nombre}' agregado exitosamente.")

    def ver_productos(self):
        if not self.products:
            print("No hay productos en el sistema.")
        else:
            for producto in self.products.values():
                print(producto)

    def eliminar_producto(self, nombre: str):
        if nombre in self.products:
            del self.products[nombre]
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print(f"El producto '{nombre}' no existe.")

    def actualizar_producto(self, nombre: str, precio: float = None, descripcion: str = None):
        if nombre in self.products:
            producto = self.products[nombre]
            if precio is not None:
                producto.precio = precio
            if descripcion is not None:
                producto.descripcion = descripcion
            print(f"Producto '{nombre}' actualizado exitosamente.")
        else:
            print(f"El producto '{nombre}' no existe.")
