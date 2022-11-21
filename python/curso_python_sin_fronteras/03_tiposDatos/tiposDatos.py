"""
tipos de datos primitivos
"""

#string
palabra = "Comillas dobles"
palabraDos = 'Comillas simples'

# enteros
numero = 10

# float
numeroFloat = 10.5

# numeros complejos
complejo = 1j

# boolean
booleano = True 
booleano = False

#print(f"\npalabra uno: {palabra} \npalabra dos: {palabraDos} \nnumero: {numero} \nfloat: {numeroFloat} \ncomplejo: {complejo} \n")


"""
listas
"""
lista = []
#print(lista)
#agregar datos a una lista de forma manual
lista = [1,2,3,4,5]

lista.append(6) # agregar datos a la lista
lista_dos = lista.copy() # generamos una copia y la asignamos a otra lista
lista.count(2) # contamos cuantas veces se repite un valor indicado
len(lista) # nos indica cuantos elementos tiene la lista
lista[0] # accedemos al valor segun la posicion del indice en la lista
lista.pop() # elimina el ultimo elemento de una lista
lista.remove(3) # indicamos que elemento queremos borrar por el valor de la lista
lista.reverse() # voltea la lista
lista.sort() # ordena la lista, solo se ordena si la lista tiene los mismos tipos de datos
lista.clear() # limpiamos toda la lista indicada


"""
Diccionarios
"""
diccionario = {
    "llaveUno": "valorUno", 
    "llaveDos": "valorDos"
}

diccionario["llaveDos"] # acceder a un dato en particular
diccionario.get('llaveUno') # accedemos a un con el metodo get
len(diccionario) # saber la contidad de elementos que tiene el diccionario
diccionario["llaveTres"] = "valorTres" # se agrega un valor a un diccionario
diccionario.pop("llaveUno") # indicamos la llave del valor que se desea eliminar
diccionario.popitem() # elimina el ultimo valor del diccionario
del diccionario["llaveDos"] # eliminar un valor por medio de la llave
diccionario_copia = diccionario.copy() # copiar el diccionario a un nuevo diccionario
diccionario_copia_dos = dict(diccionario) # otra forma de copiar el diccionario a un nuevo diccionario
diccionario.clear() # elimina todos los valores que tiene el diccionario

diccionario_armado = dict(llaveUno = "valorUno", llaveDos = "valorDos", llaveTres = 3) # contruye un diccionario

"""
Tuplas -> sin inmutables
"""
tupla = (1,2,3,4,5)
tupla.count(3) # cuenta las veces que se repite un valor en la tupla
tupla.index(2) # retorna el indice de donde se encuentra el valor indicado
lista_tupla = list(tupla) # convertimos una tupla en una lista para poder modificar los elementos


"""
Rangos
"""
rango = range(6)
print(rango)
