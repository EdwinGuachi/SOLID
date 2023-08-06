# Clase para representar un Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_informacion(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

# Clase para gestionar el Inventario de productos
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

# Función para imprimir la información de un producto
def imprimir_informacion_producto(producto):
    if producto:
        print(producto.obtener_informacion())
    else:
        print("Producto no encontrado")

# Crear instancias y probar la funcionalidad
if __name__ == "__main__":
    # Crear una instancia de Inventario para gestionar productos
    inventario = Inventario()

    # Crear instancias de Producto
    producto1 = Producto("Camiseta", 20)
    producto2 = Producto("Pantalón", 30)

    # Agregar productos al inventario
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    # Buscar y mostrar información de un producto por nombre
    producto_busqueda = inventario.buscar_producto_por_nombre("Camiseta")
    imprimir_informacion_producto(producto_busqueda)

    # Intentar buscar un producto no existente
    producto_busqueda = inventario.buscar_producto_por_nombre("Zapatos")
    imprimir_informacion_producto(producto_busqueda)
