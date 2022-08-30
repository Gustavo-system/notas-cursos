"""
funciones
"""
# las funciones se deben escribir con snake case al
# dejando dos espacios entre cada bloque de codigo
def mi_funcion():
    print("\nesto es una funcion")

mi_funcion()


# de esta forna se tipan los datos de forma descriptiva
# se requiere instalar una libreria para hacerlo fuertemente tipado
def funcion_argumentos(nombre:str):
    print(f"\nEste es tu nombre: {nombre}")

funcion_argumentos("Gustavo")


# las funciones tambien retornan un valor
# si las funciones reciben dos parametros, es obligatorio enviarlos
def sumar_datos(numeroUno:int, numeroDos:int)->int:
    return numeroUno + numeroDos

print(f"\nla suma de la funcion sumar_datos es: {sumar_datos(1,4)}")


def funcion_parametros_opcionales(*nombres):
    print(f"\nhola compañeros {nombres}")
    print(f"\nhola compañero {nombres[0]}")
    print(f"\nhola compañera {nombres[1]}")

funcion_parametros_opcionales('Gustavo', 'Ana', 'Chanchito feliz')


# se pueden mandar los parametros de la funcion por referencia al nombre y no la posicion
def funcion_inteligente(apellido:str, nombre:str):
    print("\n" + nombre, apellido)


funcion_inteligente(nombre='Chanchito', apellido='feliz')


def funcion_inteligente_dos(**kwargs):
    print("\n" + kwargs['nombre'], kwargs['apellido'])

funcion_inteligente_dos(nombre='Chanchito', apellido='super feliz')


# argumantos con un valor por defaul
def funcion_valor_defoult(nombre:str = 'chanchito'):
    print(f"\nTu nombre es: {nombre}\n")

funcion_valor_defoult("Borreguito Feliz")


# mas formas de pasar algumentos a una funcion y obtener el iterador o index
def funcion_lista(lista:list):
    for index, el in enumerate(lista, start=1):
        print(f"los animales numero {index} son : {el}")

funcion_lista(["Borreguito", "chanchito"])


def funcion_get_index(lista:list):
    index = 0
    for el in lista:
        print(f"los animales numero {index} son : {el}")
        index += 1

funcion_get_index(["Borreguito", "chanchito"])