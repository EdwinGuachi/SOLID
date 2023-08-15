class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0
        return cls._instance
    
    def increment(self):
        self.value += 1

# Crear instancias de Singleton
singleton1 = Singleton()
singleton2 = Singleton()

# Comprobar si son la misma instancia
print(singleton1 is singleton2)  # Salida: True

# Incrementar el valor en una instancia
singleton1.increment()
print(singleton2.value)  # Salida: 1
