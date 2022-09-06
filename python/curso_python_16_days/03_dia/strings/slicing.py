texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

fragmento = texto[2] # obtener el elemento con indice
print(fragmento)

fragmento = texto[2:5] # obtener el texto desde - hasta
print(fragmento)

# se puede dejar vacios algunos factores
fragmento = texto[4:] # hasta donde se pueda
print(fragmento)

fragmento = texto[:8] # desde donde se pueda hasta 8
print(fragmento)

# indicamos cada cuantos elemento se salta
fragmento = texto[1:8:2] # desde : hasta : en
print(fragmento)

fragmento = texto[::2] # desde : hasta : en
print(fragmento)

fragmento = texto[::-1] # voltemos el texto
print(fragmento)


"""
ejercicios slicing
"""

"""
Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
"Controlar la complejidad es la esencia de la programación"
"""
frase = "Controlar la complejidad es la esencia de la programación"
print(frase[0:9])

"""
Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
"Nunca confíes en un ordenador que no puedas lanzar por una ventana"
"""
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])

"""
Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
"""
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])