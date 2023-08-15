# Clase para representar una película
class Pelicula:
    def __init__(self, titulo, director, año):
        self.titulo = titulo
        self.director = director
        self.año = año

    def obtener_informacion(self):
        return f"Película: {self.titulo}, Director: {self.director}, Año: {self.año}"

# Clase para gestionar una lista de películas
class CatalogoPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar_catalogo(self):
        for pelicula in self.peliculas:
            print(pelicula.obtener_informacion())

# Crear instancias y probar la funcionalidad
if __name__ == "__main__":
    catalogo = CatalogoPeliculas()

    pelicula1 = Pelicula("El Padrino", "Francis Ford Coppola", 1972)
    pelicula2 = Pelicula("Inception", "Christopher Nolan", 2010)

    catalogo.agregar_pelicula(pelicula1)
    catalogo.agregar_pelicula(pelicula2)

    catalogo.mostrar_catalogo()
