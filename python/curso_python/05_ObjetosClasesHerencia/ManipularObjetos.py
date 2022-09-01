class Mascota:
    def __init__(self, nombre, raza) -> None:
        self.nombre = nombre
        self.raza = raza

    
    def descripcion(self):
        print(f"\nHola, el nombre de la mascota es: {self.nombre}, de raza: {self.raza}")


mascota = Mascota("iguano", "lagarto")
mascota.descripcion()

mascota.nombre = "borreguito"
mascota.raza = "esponjoso"
mascota.descripcion()

# eliminar propiedades de la instancia
del mascota.raza
# mascota.raza # marca un error por que se elimino

# eliminar un objeto entero
del mascota
#print(mascota) # marca un error de que no esta definido