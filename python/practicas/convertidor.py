def convertidor(valor_moneda:float, cantidad:float)->float:
    result = cantidad / valor_moneda
    return result

    #TODO: asi fue la primera forma de hacer un convertidor pero se realizo una optimizacion de codigo
    # result:float = 0.0
    # if tipo_moneda == 1:
    #     result = cantidad / 10.20
    #     return result
    # elif tipo_moneda == 2:
    #     result = cantidad / 19.50
    #     return result
    # elif tipo_moneda == 3:
    #     result = cantidad / 0.50
    #     return result
    # else:
    #     print('ingrese una opcion correcta')
    #     return 0


if __name__ == "__main__":
    try:
        cantidad = float(input('ingrese la cantidad a convertir: $'))
        tipo_moneda = int(input(' [1]- Bitcoin\n [2]- Dolar\n [3]- Cacahuates: '))

        if tipo_moneda == 1:
            conversion = convertidor(10.20, cantidad)
        elif tipo_moneda == 2:
            conversion = convertidor(20.0, cantidad)
        elif tipo_moneda == 3:
            conversion = convertidor(0.50, cantidad)
        else:
            print('ingrese una opcion correcta')

        print(f'\nLa conversion es {conversion}')
    except:
        print('Error, Ingrese un valor numerico')
