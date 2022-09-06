"""
metodos de string
Los string son inmutables
"""

texto = "Este es el texto a manipular"

print("\nTexto plano: ", texto, "\n")
print(f"texto en mayusculas: {texto.upper()}\n")
print(f"texto con una letra en mayuscula: {texto[5].upper()}\n")
print(f"Texto en minusculas: {texto.lower()}\n")
print(f"Separar elementos del texto: {texto.split()}\n")
print(f"Separar elementos con elemento indicado: {texto.split('t')}\n")
print(f"Unir texto: {'_'.join(texto)}\n")
print(f"Busca un determinado caracter: {texto.find('es')}\n")
print(f"Remplazar: {texto.replace('e', 'u')}\n")


"""
ejercicios con string
"""

"""
1.- Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
"Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
"""
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())


"""
2.-Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
"""
lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))


"""
3.- Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."
los siguientes pares de palabras:

"difícil" --> "fácil"
"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.
"""
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."

frase = frase.replace("difícil", "fácil")
frase = frase.replace("mala", "buena")

print(frase)