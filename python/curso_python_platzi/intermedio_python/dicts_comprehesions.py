def run():
    diccionario = {i: i**3 for i in range(1, 101)}
    # generar un diccionario sin utilizar un for multilinea
    # diccionario = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # reto -> diccionario = {i: i**3 for i in range(1, 1001) if i % 3 != 0}
    print(diccionario)


if __name__ == '__main__':
    run()