from abc import ABC, abstractmethod

# Interfaz para aves que vuelan
class IAveVolador(ABC):
    @abstractmethod
    def volar(self):
        pass

# Interfaz para aves que nadan
class IAveNadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

# Clase que implementa la interfaz de ave voladora
class PajaroVolador(IAveVolador):
    def volar(self):
        return "Volando como un pájaro"

# Clase que implementa la interfaz de ave nadadora
class PatoNadador(IAveNadador):
    def nadar(self):
        return "Nadando como un pato"

# Clase que implementa ambas interfaces
class Aguila(IAveVolador, IAveNadador):
    def volar(self):
        return "Volando alto como un águila"

    def nadar(self):
        return "No nadaré, soy un ave de presa"

# Función que realiza acciones de aves
def realizar_acciones_ave(ave):
    if isinstance(ave, IAveVolador):
        print(ave.volar())
    if isinstance(ave, IAveNadador):
        print(ave.nadar())

# Crear instancias y probar la funcionalidad
if __name__ == "__main__":
    pajaro = PajaroVolador()
    pato = PatoNadador()
    aguila = Aguila()

    realizar_acciones_ave(pajaro)  # Output: Volando como un pájaro
    realizar_acciones_ave(pato)    # Output: Nadando como un pato
    realizar_acciones_ave(aguila)  # Output: Volando alto como un águila
