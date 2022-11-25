# declaramos la clase
class Coordenada:


    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**5


if __name__ == '__main__':
    # se empieza a generar instancias
    coordenada1 = Coordenada(3, 30)
    coordenada2 = Coordenada(4, 8)

    print('Distancia entre coordenadas', coordenada1.distancia(coordenada2))
    print('Es una instancia de la clase Coordenada', isinstance(coordenada2, Coordenada))