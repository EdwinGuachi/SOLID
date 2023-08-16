# Ejemplo Simple de Patrón de Strategy:
class StrategyPago:
    def pagar(self, monto):
        pass

class PagoTarjeta(StrategyPago):
    def pagar(self, monto):
        print(f"Pago realizado con tarjeta por ${monto}")  # Beneficio 2: Mejor Diseño y Estructura

class PagoPayPal(StrategyPago):
    def pagar(self, monto):
        print(f"Pago realizado con PayPal por ${monto}")  # Beneficio 2: Mejor Diseño y Estructura

class Usuario:
    def __init__(self, estrategia_pago):
        self.estrategia_pago = estrategia_pago

    def realizar_pago(self, monto):
        self.estrategia_pago.pagar(monto)

# Uso del Patrón de Strategy:
usuario_tarjeta = Usuario(PagoTarjeta())
usuario_tarjeta.realizar_pago(100)  # Beneficio 1: Reutilización de Soluciones

usuario_paypal = Usuario(PagoPayPal())
usuario_paypal.realizar_pago(50)    # Beneficio 1: Reutilización de Soluciones
