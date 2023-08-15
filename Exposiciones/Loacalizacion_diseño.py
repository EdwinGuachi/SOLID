# Clase base para notificaciones
class Notificacion:
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje

# Clases concretas de notificaciones
class CorreoElectronico(Notificacion):
    def enviar(self):
        print(f"Enviando correo electrónico a {self.destinatario}: {self.mensaje}")

class SMS(Notificacion):
    def enviar(self):
        print(f"Enviando SMS a {self.destinatario}: {self.mensaje}")

# Clase para gestionar el envío de notificaciones
class GestorNotificaciones:
    def enviar_notificacion(self, notificacion):
        notificacion.enviar()

# Crear instancias y probar la funcionalidad
if __name__ == "__main__":
    gestor = GestorNotificaciones()

    correo = CorreoElectronico("edguachi3@espe.edu.ec", "¡Hola desde el sistema!")
    sms = SMS("+593 995351900", "¡Hola desde el sistema!")

    # Localización de decisiones de diseño: La decisión de envío está encapsulada en cada tipo de notificación.
    gestor.enviar_notificacion(correo)
    gestor.enviar_notificacion(sms)
