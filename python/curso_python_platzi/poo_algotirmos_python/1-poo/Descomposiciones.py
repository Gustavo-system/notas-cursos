# La finalidad es partir el programa en muchas partes para que se pueda formar 
# un programa en conjunto con uso de todas las clases, ademas que se puedan reutilizar
class Automovil:

    def __init__(self, modelo, marca, color, tipo_gasolina) -> None:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en reposo"
        self._motor = Motor(cilindros=4, tipo_motor=tipo_gasolina)

    
    def acelerar(self, velocidad='despacio'):
        if velocidad == 'rapido':
            self._motor.inyectar_gasolina(10)
        else:
            self._motor.inyectar_gasolina(3)

        self._estado = 'En movimientos'


class Motor:

    def __init__(self, cilindros, tipo_motor='gasolina') -> None:
        self.cilindros = cilindros
        self.tipo_motor = tipo_motor

    def inyectar_gasolina(self, cantidad):
        print(f'me inyectaron {cantidad} de gasolina para acelerar, en mi super motor de {self.tipo_motor}')


if __name__ == '__main__':
    jetta = Automovil('jetta', 'VW', 'Gris', 'Disel')
    jetta.acelerar(velocidad='rapido')