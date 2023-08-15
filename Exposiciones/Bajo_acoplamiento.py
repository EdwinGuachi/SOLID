# Clase para representar un Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

# Clase para representar un Carrito de Compras
class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.obtener_precio()
        return total

# Crear instancias y probar la funcionalidad
if __name__ == "__main__":
    carrito = CarritoCompras()

    producto1 = Producto("Camiseta", 20)
    producto2 = Producto("Pantalón", 30)

    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)

    total = carrito.calcular_total()
    print(f"Total a pagar: ${total}")
