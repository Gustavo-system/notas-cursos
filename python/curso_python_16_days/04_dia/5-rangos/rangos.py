# se utiliza para definir un numero de iteraciones en algun ciclo

# hay que tomar en cuenta que el numero final no es inclusivo
for numero in range(0, 10):
    print(numero)

print('\n')

# se le puede agregar un tercer parametro para indicar el numero de pasos que dara en la iteracion
for numero in range(0, 11, 2):
    print(numero)

# se pude usar fuera de los ciclos
lista = list(range(0,101))
print(lista)
