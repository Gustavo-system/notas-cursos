class Animal:
    def __init__(self, especie, nombre, onomatopeya):
        self.especie = especie
        self.nombre = nombre
        self.onomatopeya = onomatopeya


    def saludo(self):
        print(f"Soy un {self.especie}, mi nombre es {self.nombre} y hago {self.onomatopeya}")


class Gato(Animal):
    def __init__(self, especie, nombre, onomatopeya):
        Animal.__init__(self, especie, nombre, onomatopeya)
        print("soy un gato extendido")

    def saludoGato(self):
        return super().saludo()


class Perro(Animal):
    def __init__(self, especie, nombre, onomatopeya):
        super().__init__(especie, nombre, onomatopeya)
        print("soy un perro extendido")

    def saludoPerro(self):
        return super().saludo()


gato = Gato("gato", "peluza", "miaaauuu")
gato.saludoGato()

perro = Perro("perro", "guacamayo", "guau guau")
perro.saludoPerro()