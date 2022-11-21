"""
propiedades de string

- se pueden poner triple comilla para poder dar saltos de linea como en este ejemplo
"""

# concatenacion
nombre, raza = "bumbuble", "autobot"
print(nombre + raza)

# se pueden multiplicar los string
print(nombre*5)

saltos_de_lineas = """Así se pueden hacer saltos 
    de lineas, para poder hacer textos
"""
print(saltos_de_lineas)

# si se encuentra una palabra en una cadena de texto
print("bum" in nombre)

# doble negacion
print("auto" not in raza)

# conocer el largo de un string
print(len(nombre))


"""
ejercicios
"""


"""
1.- Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, 
conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
"""
print("Repetición"*15)


"""
2.- Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
Tierra mojada,
mis recuerdos de viaje
entre las lluvias
"""
frase = """
Tierra mojada,
mis recuerdos de viaje
entre las lluvias
"""
print("agua" not in frase)


"""
Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
"""
palabra = "electroencefalografista"
print(len(palabra))