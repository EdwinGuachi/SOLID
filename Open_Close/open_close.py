from enum import Enum

# Enum para los tipos de vehículo
class TipoVehiculo(Enum):
    AUTO = 1
    MOTOCICLETA = 2

# Clase Vehiculo
class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

# Funciones para pintar un auto y una motocicleta
def pintar_auto(vehiculo):
    print("Pintando Auto.")

def pintar_motocicleta(vehiculo):
    print("Pintando Motocicleta.")

# Función pintar que utiliza polimorfismo
def pintar(vehiculo):
    if vehiculo.tipo == TipoVehiculo.AUTO:
        pintar_auto(vehiculo)
    elif vehiculo.tipo == TipoVehiculo.MOTOCICLETA:
        pintar_motocicleta(vehiculo)

# Creación de instancias de las clases
auto = Vehiculo(TipoVehiculo.AUTO)
motocicleta = Vehiculo(TipoVehiculo.MOTOCICLETA)

# Llamamos a la función pintar para pintar cada vehículo
pintar(auto)
pintar(motocicleta)