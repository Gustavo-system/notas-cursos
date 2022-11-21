# Analizador de textos

# 0 Solicitar un texto y que se retornen los siguientes puntos:
# 1 Cuantas veces aparece el las letras que el usuario desea buscar
# 2 Cuantas palabras tiene el texto ingresado
# 3 Informar cual es la primera y la ultima letra del texto
# 4 Convertir el texto al reves
# 5 indicar si existe la palabra "python" dentro del texto ingresado

# 0
texto_ingresado = input("\ningrese el texto que desee que se analice: ")

# 1
letra1 = input('\nIngrese la primera letra que desea buscar: ')
letra2 = input('Ingrese la segunda letra que desea buscar: ')
letra3 = input('Ingrese la tercera letra que desea buscar: \n')

contador_letra1 = 0
contador_letra2 = 0
contador_letra3 = 0

for letra in texto_ingresado:
    if letra1.lower() == letra.lower():
        contador_letra1 += 1
    elif letra2.lower() == letra.lower():
        contador_letra2 += 1
    elif letra3.lower() == letra.lower():
        contador_letra3 += 1

print(f'La letra {letra1.upper()} se repite {contador_letra1} veces')
print(f'La letra {letra2.upper()} se repite {contador_letra2} veces')
print(f'La letra {letra3.upper()} se repite {contador_letra3} veces')

# 2 
texto_split = texto_ingresado.split(" ")
print('\nEl numero de palabras que tiene el texto es:', len(texto_split))

# 3
print('\nprimera letra:', texto_ingresado[0])
print('ultima letra:', texto_ingresado[-1])

# 4
print('\nTexto en reverso:', texto_ingresado[::-1])

# 5
in_texto_python = 'python' in texto_ingresado.lower()
print('\nLa palabra python esta dentro del texto ingresado:', in_texto_python)
