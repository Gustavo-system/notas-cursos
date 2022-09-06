"""
archivos
"""

"""
permisos

r = read
a = append
w = write

"""

# como segundo parametro del metodo open se pasan los permisos
archivo = open('archivo.txt', 'r')
print(archivo.read())