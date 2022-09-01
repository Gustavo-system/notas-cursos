class Mascota:
    def __init__(self, nombre, raza) -> None:
        self.nombre = nombre
        self.raza = raza

    
    def descripcion(self):
        print(f"\nHola, el nombre de la mascota es: {self.nombre}, de raza: {self.raza}")


mascota = Mascota("iguano", "lagarto")

mascota.descripcion()