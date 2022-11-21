# Python

## Punto de entrada

Ejecuta todo lo que esta debajo del entrypoint se puede tener codigo antes del punto de entrada y no sera ejecutado, se pueden declarar funciones o otras acciones

```
if __name__ == '__main__':
	# codigo
```

## Variables

Declaracion de variables, la documentación de python dice que las variables se deben declarar con la sintaxis de snakecase, esto quiere decir que si la variable tiene mas de una palabra se debe separar con un "\_" y nunca declarar variables con numeros al inicio

```
nombre = "valor"
edad = 21
```

Puede cambiar su valor sin previo aviso

```
nombre = "Pablo"
nombre = "Ana"
edad = 23
```

Multiples variables en una sola linea

```
a, b, c = "lala" , "lele", "lili"
```

## Constantes

Se declaran en mayusculas y su valor no deberia cambiar a lo largo del programa, un ejemplo de esto es el valor del PI, cuando se requiere calcular al area de un circulo.

```
PI = 3.1416
```

## Tipos de datos

### String

se utlizan comillas dobles o sencillas, se pueden usar en conjunto en caso de que ase se necesite

```
saludo = "Hola mundo"
frase = "Ella me dijo 'Hola'"
```

se utliza el slash invetido (\) para que pyton haga caso omiso sobre las comillas dentro de las comillas de la cadena

```
frase = 'Ella me dijo "Hola" '
frase "Ella me dijo \"Hola\" "
```

### Boolean

Solo tiene dos valores True and False, se utilizan para poder generar condicionales

```
is_true = true
is_false = false
```

### Int

Tipo de dato para almecer valores enteros

```
edad = 21
```

### Float

decimal = 1.0

### Double

decimal = 1.0

## Operadores Artirmeticos

-   suma +
-   resta -
-   multiplicacion \*
-   divicion /
-   divicion entera //numero
-   potencia \*\*numero
-   incremento ++
-   decremento --
-   modulo %

## Operadores de comparacion

-   menor que <
-   mayor que >
-   menor igual <=
-   mayor igual >=
-   igual ==
-   distintos !=

## Operadores logicos

-   y = and
-   o = or

## Concatenacion
