"""
sets
- solo admite elementos unicos, no hay ningun elemento repetido en el set
- no estan ordenados en indices
- sus elementos son inmutables
- no se pueden agregar listas o diccionarios
- si admite tuplas por que ambos son inmutables
"""

mi_set = set({1,2,3,4,5})

print("\n", type(mi_set))
print(mi_set)

otro_set = {1,2,3,4,6}
print("\n", type(otro_set))
print(otro_set)

print('\nlongitud de mi set', len(mi_set))
print('saber si el valor 2 se encuentra en mi_set =', 2 in mi_set)

set_unido = mi_set.union(otro_set)
print("la union de dos sets", set_unido)

set_unido.add(7)
print("se agrego un elemento al set_unido", set_unido)
set_unido.remove(1)
print("se elimino el elemento 1 en el set_unido", set_unido)
set_unido.discard(1)
print("se descarta el elemento 1 en el set_unido, pero como ya borro no afecta", set_unido)
set_unido.pop() # elimina un elemento aleatorio
print("se elimina un elemento aleatorio con el .pop()", set_unido)
set_unido.clear()
print("se limpio nuestro set con el .clear()", set_unido)



