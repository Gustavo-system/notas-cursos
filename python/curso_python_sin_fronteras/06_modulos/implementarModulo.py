"""
Modulos
"""
# importamos el modulo en donde se separa la logica
import modulos

# accedemos a los valores un modulo
print(modulos.mascota)
modulos.saludo("Borreguito")


# renombrar modulos
import modulos as mod
print(mod.mascota)
mod.saludo("Leon")

# importar cosas seleccionadas de un modulo
from modulos import saludo
saludo("Lobo")