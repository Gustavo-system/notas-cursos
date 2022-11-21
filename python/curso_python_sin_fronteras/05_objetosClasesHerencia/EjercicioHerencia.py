class Animal:
    def __init__(self, especie, nombre, onomatopeya):
        self.especie = especie
        self.nombre = nombre
        self.onomatopeya = onomatopeya


    def saludo(self):
        print(f"Soy un {self.especie}, mi nombre es {self.nombre} y hago {self.onomatopeya}")


class Gato(Animal):
    def saludoGato(self):
        return super().saludo()


class Perro(Animal):
    def saludoPerro(self):
        return super().saludo()


gato = Gato("gato", "peluza", "miaaauuu")
gato.saludoGato()

perro = Perro("perro", "guacamayo", "guau guau")
perro.saludoPerro()