from enum import Enum

# Enum para los tipos de vehículo
class TipoVehiculo(Enum):
    AUTO = 1
    MOTOCICLETA = 2

# Clase Vehiculo (clase base)
class Vehiculo:
    def pintar(self):
        pass

# Clase Auto (hereda de Vehiculo)
class Auto(Vehiculo):
    def pintar(self):
        print("Pintando Auto.")

# Clase Motocicleta (hereda de Vehiculo)
class Motocicleta(Vehiculo):
    def pintar(self):
        print("Pintando Motocicleta.")

# Función pintar que utiliza polimorfismo
def pintar(vehiculo):
    vehiculo.pintar()

if __name__ == "__main__":
    auto = Auto()
    motocicleta = Motocicleta()

    pintar(auto)  # Salida: Pintando Auto.
    pintar(motocicleta)  # Salida: Pintando Motocicleta.