from abc import ABC, abstractmethod

# Interfaz para las estrategias de pago
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

# Estrategias concretas de pago
class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con tarjeta de crédito")

class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con PayPal")

class TransferenciaBancaria(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con transferencia bancaria")

# Cliente
class Cliente:
    def __init__(self, metodo_pago):
        self.metodo_pago = metodo_pago

    def realizar_compra(self, monto):
        self.metodo_pago.procesar_pago(monto)

# Uso de diferentes estrategias de pago
tarjeta = TarjetaCredito()
paypal = PayPal()
transferencia = TransferenciaBancaria()

cliente1 = Cliente(tarjeta)
cliente1.realizar_compra(100)

cliente2 = Cliente(paypal)
cliente2.realizar_compra(50)

cliente3 = Cliente(transferencia)
cliente3.realizar_compra(200)
