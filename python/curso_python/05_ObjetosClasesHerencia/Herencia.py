class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def descripcion(self):
        print(f"\nmi nombre es {self.nombre} {self.apellido}")



# se aplica herencia para reutilizar funcionalidad
class Admin(Usuario): # asi se defina que hereda de otra clase
    def descripcionAdmin(self):
        print(f"Mi nombre es: {self.nombre} y mi puesto es administrador")


# tambien hereda el metodo __init__(): por eso se le pasan argumentos
admin = Admin(nombre="Chanchito", apellido="Feliz")
admin.descripcion()
admin.descripcionAdmin()


""" 
la clase padre no puede acceder a los metodos de las clases hijas, pero las clases hijas si a los metodos padre
"""