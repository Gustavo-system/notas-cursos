def is_palindrome(palabra:str) -> bool:
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]


def run():
    palabra = input("ingrese una palabra para saber si es un palindromo: ")
    palindrome = is_palindrome(palabra)
    if palindrome:
        return print(f'la palabra { palabra } es un palindromo')
    return print(f'la palabra { palabra } no es un palindromo')


if __name__ == "__main__":
    run()