# Creamos una clase para representar un Estudiante
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Creamos una clase separada para manejar la persistencia (almacenamiento) de los estudiantes
class AlmacenamientoEstudiantes:
    def guardar_en_bd(self, estudiante):
        # Simulamos el proceso de guardar en una base de datos
        print(f"Guardando {estudiante.obtener_informacion()} en la base de datos")

# Creamos una clase para manejar la lógica de negocios relacionada con los estudiantes
class LogicaEstudiantes:
    def __init__(self):
        self.almacenamiento = AlmacenamientoEstudiantes()

    def agregar_estudiante(self, estudiante):
        # Aquí se agrega la lógica de validación, cálculos, etc.
        print(f"Agregando estudiante: {estudiante.obtener_informacion()}")
        self.almacenamiento.guardar_en_bd(estudiante)

# Crear instancias y probar la funcionalidad
if __name__ == "__main__":
    estudiante1 = Estudiante("Juan", 20)
    estudiante2 = Estudiante("María", 22)

    logica_estudiantes = LogicaEstudiantes()
    logica_estudiantes.agregar_estudiante(estudiante1)
    logica_estudiantes.agregar_estudiante(estudiante2)