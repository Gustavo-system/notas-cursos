# list comprehensions
def run():
    lista = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(lista)
    # reto, crea una lista con todos los multiplos de 4 que tambien sean multiplos de 
    # 6 y de 9 hasta cinco dijitos
    numbers = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print('reto', numbers)

if __name__ == "__main__":
    run()