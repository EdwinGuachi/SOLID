from abc import ABC, abstractmethod
#estructura comun para multiples clases
class BebidaTemplate(ABC):
    def preparar(self):
        self.calentar_agua()
        self.agregar_ingredientes()
        self.servir_en_taza()
        self.agregar_aderezos()

    @abstractmethod
    def calentar_agua(self):
        pass

    @abstractmethod
    def agregar_ingredientes(self):
        pass

    @abstractmethod
    def servir_en_taza(self):
        pass

    def agregar_aderezos(self):
        pass

class Te(BebidaTemplate):
    def calentar_agua(self):
        print("Calentando agua")

    def agregar_ingredientes(self):
        print("Agregando hojas de té")

    def servir_en_taza(self):
        print("Sirviendo té en la taza")

class Cafe(BebidaTemplate):
    def calentar_agua(self):
        print("Calentando agua")

    def agregar_ingredientes(self):
        print("Agregando café molido")

    def servir_en_taza(self):
        print("Sirviendo café en la taza")

    def agregar_aderezos(self):
        print("Agregando azúcar y leche")

# Preparación de bebidas
print("Preparando té:")
te = Te()
te.preparar()

print("\nPreparando café:")
cafe = Cafe()
cafe.preparar()
