"""
Diccionarios
"""

diccionario = {
    'nombre' : 'Chanchito',
    'apellido' : 'Feliz',
    'edad' : 20,
    'vivo' : True,
    'puntos': [10, 20, 34],
    'direccion' : {
        'calle' : 'calle uno',
        'estado' : 'feliz',
        'numero': 1
    }
}

print("\n", type(diccionario))

# consultar el contenido
print(diccionario["nombre"])
print(diccionario.get("edad"))
print(diccionario["puntos"][1])
print(diccionario["direccion"]["calle"])
print(diccionario["direccion"]["estado"].upper())

# agregar elementos a un diccionario
diccionario['deporte_favorito'] = 'Basquetbool'
print(diccionario)
diccionario['edad'] = 23
print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())