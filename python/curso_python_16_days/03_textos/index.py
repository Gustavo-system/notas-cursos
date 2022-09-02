# acceder a los indices del texto
mi_texto = "Indices"
indice_uno = mi_texto[0]
print(indice_uno)

indice_uno = mi_texto.index("n") # tambien se pueden buscar palabras y es sensible a minusculas y mayusculas
print(indice_uno)

indice_uno = mi_texto.index("e", 3, 6) # a buscar, desde, hasta -> esos son los parametros
print(indice_uno)

indice_uno = mi_texto.rindex("d") # busca de izquierda a derecha
print(indice_uno)

"""
Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
"""
palabra = "ordenador"
print(palabra[4])

"""
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
"""
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))
print(frase.rindex("práctica"))
