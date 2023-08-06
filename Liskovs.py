class Ave:
    def volar(self):
        pass

class Pajaro(Ave):
    def volar(self):
        return "Volando como un pájaro"

class Avion(Ave):
    def volar(self):
        return "Volando como un avión"

def realizar_vuelo(ave):
    return ave.volar()

# Crear instancias y probar la funcionalidad
if __name__ == "__main__":
    pajaro = Pajaro()
    avion = Avion()

    print(realizar_vuelo(pajaro))  # Output: Volando como un pájaro
    print(realizar_vuelo(avion))   # Output: Volando como un avión