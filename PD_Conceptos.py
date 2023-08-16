# Los patrones de diseño son soluciones reutilizables para problemas de diseño comunes en POO.
# Proporcionan una guía para resolver problemas y mejorar la estructura y flexibilidad del código.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0
        return cls._instance

# Uso del Singleton
obj1 = Singleton()
obj1.value = 10

obj2 = Singleton()
print(obj2.value)  # Salida: 10 (misma instancia que obj1)
