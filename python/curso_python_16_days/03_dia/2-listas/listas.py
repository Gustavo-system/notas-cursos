"""
- Las listas pueden estar compuestas por distintos tipos de datos
- Se escriben entre corchetes
- Estan separados entre si por comas ( , )
- Se pueden anidar listas
- Son mutables
"""

mi_lista = ['a', 'b', 'c']
mi_lista_dos = ['d', 'e', 'f']

print("tipo de lista", type(mi_lista))
print("tamaño de la lista", len(mi_lista))
print("elemento en la posicion 0 =", mi_lista[0])
print("ver solo elementos por rango =", mi_lista[1:3])

print("se concatenan las listas", (mi_lista + mi_lista_dos))

mi_lista[1] = "nuevo valor"
print(mi_lista)

mi_lista_dos.append('g')
print("se agrego un elemento a la lista dos", mi_lista_dos)

mi_lista.pop(0)
print("se elimino un elemento por el indice en la lista", mi_lista)


eliminado = mi_lista.pop(1)
print("este es el elemento eliminado:", eliminado)

lista_desordenada = [1,8,3,7,4,2,78,11,10]
lista_desordenada.sort()
print("Ordena la lista pero no retornar un valor:", lista_desordenada)

lista_desordenada.reverse()
print("Voltear una lista con el reverse():", lista_desordenada)