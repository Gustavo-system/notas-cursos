class Usuario:
    # esta funcion es el contructor de la clase
    # siempre se ejecuta primero sin ninguna exepcion
    def __init__(self, nombre, apellido):
        # asi se inicializan los valores
        # self es una referencia de la clase
        self.nombre = nombre
        self.apellido = apellido


# se genera una instancia
usuario = Usuario("chanchito", "feliz")
usuario2 = Usuario("borreguito", "feliz")

print(f"usuario 1: {usuario.nombre} {usuario.apellido}\nusuario 2: {usuario2.nombre} {usuario2.apellido}")