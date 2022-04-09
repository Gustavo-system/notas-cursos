"""
Trabajando con cadenas de texto en python
"""
nombre = 'gustavo'

print(f'upper pone todas las letras en mayuscula {nombre.upper()}')
print(f'capitalize pone la primera letra en mayuscula {nombre.capitalize()}')
print(f'strip elimina espacios al inicio y al final del texto {nombre.strip()}')
print(nombre.replace('a', 'e'))
print(f'strip elimina espacios al inicio y al final del texto {nombre[5]}')
print(f'strip elimina espacios al inicio y al final del texto {len(nombre)}')

# texto.replace('', '')				-> remplasa el primer parametro por el parametro dos
# texto[posicion]						-> retorna la letra que este en la posicion indicada en el texto
# len(texto)

"""
Rebanadas de texto
"""

palabra = 'Rebanada'

print(palabra[1:5])
print(palabra[:5])
print(palabra[0:5:2])


print(10 / 2 + 5 * 7)
print(round(10.3456, 2))