"""
sencia de flujo -> if, elif, else


tipos de evaluaciones:

igual           ==
distinto        !=
mayor que       >
menos que       <
mayor igual     >=
menor igual     <=
incremento      +=
decremento      -=


sintaxis:

if evaluacion:
    flujo
elif evaluacion:
    flujo
else:
    flujo

"""

numeroUno, numeroDos = 5, 3

if numeroUno > numeroDos:
    print("5 es mayor que tres")
elif numeroUno < numeroDos:
    print("5 es menos que tres")
else:
    print("el numero no se sabe cual es")


# if corto, operador ternario
if 2 < 5: print('if de una sola linea')

es_mayor = "es mayor que el numero dos" if numeroUno > numeroDos else "es menor que el numero dos"
print(es_mayor)


"""
operadores logicos -> and, or
"""
if 2 < 5 and numeroUno > numeroDos:
    print("con el 'and' se deben cumplir ambas condiciones para retornar true")

if 2 < 5 or numeroUno > numeroDos:
    print("con el 'or' se debe cumplir solo una para retornar true")