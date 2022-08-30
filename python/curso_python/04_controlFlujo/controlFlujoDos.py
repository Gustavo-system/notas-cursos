"""
loops
"""

#while
iterador = 0

while iterador <= 5:
    print(f"ronda Numero: {iterador}")
    iterador += 1


iterador_dos = 0

while iterador_dos <= 5:
    iterador_dos += 1
    if iterador_dos == 3:
        continue
    print(f"while dos, ronda {iterador_dos}")



iterador_tres = 0

while iterador_tres < 5:
    iterador_tres += 1
    if iterador_tres == 3:
        break
    print(f"while tres, ronda: {iterador_tres}")


# for
animales = ['Chanchito feliz', 'gato perro', 'conejo rabioso']

print("\nanimales")
for animal in animales:
    print(animal)

print("\nbuscando animal")
for animal in animales:
    print(animal)
    if animal == "conejo rabioso":
        print(f"el animal '{animal}' si se encontro")
        break

print("\niterador con range")
# se puede usar el range para indicar cuantas veces se quiere iterar
for iterador in range(1, 11): # en este caso el rango maximo no se incluye y siempre queda -1
    print(iterador)

print("\ndel 1 al 10 de 2 en 2")
for iterador in range(0, 11, 2): # si se le pasa un tercer parametro es la cantidad de saltos que dará
    print(iterador)

#se puede usar el else y se ejecutara siempre al final del loop for
print("\nSe puede agregar el else al loop for")
for iterador in range(0,11,2):
    print(iterador)
else:
    print("se termino de recorrer el loop for")