# Operadores logicos

"""
Cuando se utiliza and quiere decir que ambas condiciones deben cumplirce
y = and

Cuando se utiliza 'or' quiere decir que alguna de las condiciones debe cumplirce
o = or

Es la negacion de las condiciones
no = not
"""

# retorna falso por que las dos se deben cumplir
mi_bool = (4 < 5) and (5 == 2)
print(mi_bool)

# retorna verdadeto por que ambas son correctas
mi_bool = (4 < 5) and (5 == (2 + 3))
print(mi_bool)

# retorna Verdadero por que se debe cumplir al menos una de las dos
mi_bool = (4 < 5) or (5 == 2)
print(mi_bool)

# retorna verdadero por que ambas se cumplen
mi_bool = (4 < 5) or (5 == (2 + 3))
print(mi_bool)

# es la negacion de la condicional
mi_bool = not (5 == 2)
print(mi_bool)