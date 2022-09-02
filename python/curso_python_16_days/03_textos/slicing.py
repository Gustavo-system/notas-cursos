texto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

fragmento = texto[2] # obtener el elemento con indice
print(fragmento)

fragmento = texto[2:5] # obtener el texto desde - hasta
print(fragmento)

# se puede dejar vacios algunos factores
fragmento = texto[4:] # hasta donde se pueda
print(fragmento)

fragmento = texto[:8] # desde donde se pueda hasta 8
print(fragmento)

# indicamos cada cuantos elemento se salta
fragmento = texto[1:8:2] # desde : hasta : en
print(fragmento)

fragmento = texto[::2] # desde : hasta : en
print(fragmento)

fragmento = texto[::-1] # voltemos el texto
print(fragmento)

