# Los patrones de diseño se dividen en tres categorías principales: creacionales, estructurales y de comportamiento.

# Patrón Creacional - Fábrica
class Producto:
    def operacion(self):
        pass

class ProductoA(Producto):
    def operacion(self):
        print("Operación en Producto A")

class Fabrica:
    def crear_producto(self):
        pass

class FabricaA(Fabrica):
    def crear_producto(self):
        return ProductoA()

fabrica_a = FabricaA()
producto_a = fabrica_a.crear_producto()
producto_a.operacion()

# Patrón Estructural - Adaptador
class Adaptable:
    def metodo_adaptable(self):
        pass

class ClaseAdaptada(Adaptable):
    def metodo_adaptable(self):
        print("Método en Clase Adaptada")

class Adaptador:
    def __init__(self, clase_adaptada):
        self.clase_adaptada = clase_adaptada

    def metodo_adaptable(self):
        self.clase_adaptada.metodo_adaptable()

clase_adaptada = ClaseAdaptada()
adaptador = Adaptador(clase_adaptada)
adaptador.metodo_adaptable()

# Patrón de Comportamiento - Estrategia
class Estrategia:
    def ejecutar(self):
        pass

class EstrategiaA(Estrategia):
    def ejecutar(self):
        print("Ejecutando Estrategia A")

class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def ejecutar_estrategia(self):
        self.estrategia.ejecutar()

estrategia_a = EstrategiaA()
contexto = Contexto(estrategia_a)
contexto.ejecutar_estrategia()
