"""
Tuplas
- son inmutables
- ocupan menos espacios de momoria
- se usan para almacenar estruccturas que no queremos que sean modificadas
"""

mi_tupla = (1, True, False, [10,20,30], {'nombre':'chanchito', 'edad': 18}, (1,2,3,4,5), 'Tupla')

print("\n", type(mi_tupla))

# consultar
print(mi_tupla[0])
print(mi_tupla[-3])
print(mi_tupla[-2])
print(mi_tupla[5][2])


# convertir una tupla a una lista
mi_tupla = list(mi_tupla)
print("\nse cambio el tipo de tupla a lista", type(mi_tupla))
mi_tupla = tuple(mi_tupla)
print("\nse cambia la lista a una tupla", type(mi_tupla))


# deben tener el mismo numero de valores que variables declaradas
tuplita = (1,2,3)
x,y,z = tuplita
print(x, y, z, "\n")


print('longitud de la tupla ->', len(mi_tupla))
print('cuantas veces aparece el numero 2 en mi_tupla ->', mi_tupla.count(2))
print('encontrar la posicion del valor False en mi_tupla ->', mi_tupla.index(False))