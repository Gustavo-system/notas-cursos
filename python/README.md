# Python

## Punto de entrada

Ejecuta todo lo que esta debajo del entrypoint se puede tener codigo antes del punto de entrada y no sera ejecutado, se pueden declarar funciones o otras acciones

```
if __name__ == '__main__':
	# codigo
```

## Imprimir datos en consola

Se utliza un metodo reservado llamado print(), al cual se le indica lo que se imprime dentro de los parentecis, en el se pueden imprimir variables o textos.

```
print("Hola mundo")
```

## Tipos de datos

### String

se utlizan comillas dobles o sencillas, se pueden usar en conjunto en caso de que ase se necesite

```
saludo = "Hola mundo"

frase = "Ella me dijo 'Hola'"
```

se utliza el slash invetido \ para que pyton haga caso omiso sobre las comillas dentro de las comillas de la cadena

```
frase = 'Ella me dijo "Hola" '

frase "Ella me dijo \"Hola\" "
```

### Boolean

Solo tiene dos valores True and False, se utilizan para poder generar condicionales

```
is_true = True

is_false = False
```

### Int

Tipo de dato para almecer valores enteros

```
edad = 21
```

### Float

```
variable_float = 1.0
```

### Double

```
variable_double = 1.0
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

## Comentarios

Se utilizan para documentacion breve del codigo que se esta escribiendo con el fin de que los proximos desarrolladores tenga una mayor claridad de la funcion del codigo, python no interpreta estas lineas de codigo al momento de la ejecucion.

```
# Comentario de una sola linea

"""
	Comentario multilinea
"""
```

## Concatenacion

Es para unir dos textos, para las concatenaciones se utiliza el singo de suma (+), solo se debe tener en consideracion los tipos de datos que se desean concatenar

```
nuevo_valor = variable1 + variable2
```

otra manera en la que podemos concatenar es anteponiendo la letra "f" que tiene un significado de formato, con eso se debe hacer uso de los corchetes "{}" en los cuales dentro de ellos se pone la variable deseada

```
nuevo_valor = f'texto { variable }'
```

## Manipulacion de cadenas de carateres

Metodos que nos permiten manipular un string, apesar que es un tipo de dato innmutable, nos permite modificarlo en tiempo de ejecucion sin cambiar su verdadero valor.

```
texto = "hola"

print(texto * 3) 			#HolaHolaHola
texto.upper() 				#Convierte en mayusculas el texto
texto.lower()				#Convierte en minusculas el texto
texto.capitalize()			#Convierte la primera letra en mayuscula
texto.strip()				#Borra espacios al incio y al final de la cadena
texto.replace('', '') 		#Remplasa el primer parametro por el parametro dos
texto.split('valor')		#Separa el texto por el caracter indicado entre los parentesis
texto[posicion] 			#Retorna la letra que este en la posicion indicada en el texto
len(texto) 					#Nos indica la longitud del texto
texto[::-1] 				#Voltear un string
text[0:3] 					#Recortamos el texto del indice 0, al indice 3
texto[1:7:2] 				#Recortamos el texto del indice 1 al indice 7 en pasos de 2 en 2
texto.find('ex')			#Busca un determinado caracter
'_'.join(texto)				#Unir texto
```

## Conversiones

Se utiliza para converit un tipo de dato a otro, para poder realizar distintas operaciones que se requieran y no se pueda por errores de tipado

Para convertir un valor a un string se utiliza el metodo str()

```
str(numero)
```

Convierte un numero en string a un numero de tipo int()

```
int(string)
```

#### Saber que tipo de dato es la variable

```
type(variable)
```

## Leer datos por consola

Se utiliza el metodo input(), dentro de sus parentecis se proporciona el mensaje que se mostrara en la consola haciendo alucion a lo que se requiere ingresar, se debe tener en cuenta que todo dato que se ingrese se asigna como un string

```
variable = input('texto que indica que valor debe ingresar')
```

## Estructuras de control

Nos ayudan a saber que camino tomara nuestro flujo del programa

== Estructura basica de IF ==

if valor operedor valor:
bloque de codigo
elif condicion:
bloque de codigo
else:
bloque de codigo

== IF anidados ==

if valor operador valor
bloque de codigo
if valor operador valor
bloque de codigo
else:
bloque de codigo
else:
bloque de codigo

== IF corto ==

if condicion: bloque de codigo else: bloque de codigo

** CICLOS / LOOPS **

> > > Nos ayuda a repetir codigo un sierto tipo de veces, existen dos tipos de ciclos while y for

== Sintaxis basica WHILE ==

while condicion:
bloque de codigo
condicion a cumplir

== Sintaxis de FOR ==

for variable_referencia in list/dict:
bloque de codigo
else:
bloque de codigo

** Break **

> > > La palabra reservada break, rompe el ciclo cuando se cumple la condicion

list_numero = [1,2,3,4,5,6,7,8,9,10]

for numero in list_numero:
if numero > 5: -> esto nos devuelve el valor del 1 al 5 sin ejecutar mas
break
print (numero)

** Continue **

> > > la palabra reservada continue no para el ciclo solo salta el valor seleccionado

for numero in list_numero:
if numero == 5:
continue -> esto nos muestra todos los numero del 1 al 10 menos el 5
print (numero)

** Rango **

> > > nos permiten tener muchos lementos desde un numero inicial hasta un numero final que nosotros le proporcionamos

rango = rango(6) -> nos devuelve rango(0,6) en una lista

** Funciones **

> > > para llamar a una funcion se escribe el nombre de la funcion seguido de parentesis
> > > para declarar una funcion se utiliza la palabra reservada "def"

nombreFuncion() -> funcion sin parametros
nombreFuncion(parametros) -> funcion con parametros

> > > Declaracion de funciones

def nombreFuncion(): -> funcion sin parametros
bloque de codigo

def nombreFuncion(parametros): -> funcion con parametros
bloque de codigo

def nombreFuncion(\*argumento) -> los argumentos son variables y se imprimen como una tupla
bloque de codigo

def nombrefuncion(\*\*kbargs) -> funciones como diccionario
bloque de codigo

** Indices **

> > >     Los indices indican la posicion de un elemento en una lista o en una cadena

    para conocer el indice de un elemento su puede usar el objeto .index()
    el cual devuelve la posiscion en donde esta ubicadao ese elemento

list_vocales[a,e,i,o,u]
lista_vocales.index("e") -> esto devuelve la posicion = 1

> > > para conocer que elemeto esta en la posicion se utiliza la siguiente sintaxis

list_vocales[3] -> nos devuelve = o

> > > se puede utilizar posiciones negativas
> > > lista_vocales[-1] -> nos devuelve = u

** palabra reservada del **

> > > Esto elimina variables si queremos borrar una variable o elementos de una lista utilizamos (del)

    pero no se puede modificar el valor de una cadena

del variable -> elimina la variable
del list[0] -> elimina la posicion que se le indique de la lista

** PALABRA IN and NOT **

> > > Esta palabra reservada nos devuelve verdadero y falso, corrobora que exista un elemento en la lista o en la cadena
> > > letra in cadena -> nos devuelve true or false
> > > valor in lista -> nos devuelve true or false

> > > se puede utilizar la palabra reservada (not) para corroborar que no exista el elemento, tambien devuelve un verdadero o un falso
> > > letra not cadena -> nos devuelve un true or false
> > > valor not list -> nos devuelve un true or false

---

**\*** ESTRUCTURAS DE DATOS **\***

---

** Listas / Array **

[valor1, valor2, valor3,...] -> nombrelista = [1,2,3,4,5]

para agredar elementos a las listas de forma manual

nombreLista = nombreLista + [nuevoValor, nuevoValor,...]
nombreLista += [nuevoValor, nuevoValor,...] -> se utiliza la suma asignacion, es forma corta de hacer lo de la linea anterior

lista = [1,2,3,4,5]
lista += [6,7] -> da como resultado [1,2,3,4,5,6,7]

> Para acceder al indice de una lista se incia desde el 0
> lista[0] -> nos devuelve el valor de 1

== metodos disponibles en las listas ==

lista.append(valor) -> .append(valor) Para agregar un valor
lista.extend(valor1,valor2) -> .extend(valores) Para agregar multiples valores
lista.remove(valor) -> .remove(valor) Para remover un elemento especifico
lista.clear() -> .clear() Limpiar toda la lista
lista.pop() -> .pop() Para eliminar el ultimo elemento
lista.count(valor) -> .count(valor) Para contar las veces que se repite el valor indicado en la lista
lista.reverse() -> .reverse() Ordenada de forma inversa la lista
lista.sort() -> .sort() Ordena la lista de menor a mayor exepto si son datos de distinto tipo
nueva_lista = lista.copy() -> .copy() Para hacer una copia exacta de la lista
len(lista) -> len() Para saber la longitud (numero de elementos) que tiene la lista

> > > podemos utilizar la palabra reservada (list()), sin embargo este objeto solo acepta un parametro
> > > para poder ingresar varios valores como en una lista normal se usa la siguiente sintexis

list([valor1, valor2, ...])

> > > si ponemos una palabra dentro de list

list("Gus") -> el resultado es: ['G','u','s']

** Diccionarios / objetos / json **

diccionario = {
"llave1": "valor1",
"llave2": "valor2",
"llave3": "valor3",
}

diccionario['llave'] -> accedemos a travez de string
diccionario.get('llave') -> se puede utilizar el metodo get para acceder a los datos
diccionario['llave'] = 'nuevo_valor' -> para cambiar los valores del diccionario
diccionario['nueva_llave'] = 'valor' -> agregar valores al diccionario
diccionario.pop('llave') -> eliminar un elemento del diccionario
diccionario.popitem() -> se elimona el ultimo elemento agregado
diccionario.items() -> devuelve los pares clave-valor del diccionario
diccionario.copy() -> copiamos el diccionario
diccionario.clear() -> limpiamos todo el diccionario
del diccionario['valor'] -> eliminamos el valor del diccionario
len(diccionario) -> para saber la longitud del diccionario

=== Diccionarios Anidados ===

dict = {
"llave" : {
"llave": valor,
"llave2": valor2,
},
}

** Tuplas **

> Las tuplas una vez creadas no se pueden modificar

tupla = ('valor1', 'valor2', 'valor3', ...)

tupla.count() -> numero de elementos que tiene la tupla
tupla.index() -> devuelven la posicion del elemento ( indice del elemeto )
lista_tupla = list(tupla) -> para poder alterar la tupla se debe convertir a una lista y usar los metodos de la lista

** Entornos Virtuales **

py -m venv nombre_venv -> creamos un ambiente virtual
.\venv\Script\activate -> activamos el entrono virtual en windows
source venv/bin/activate -> activamos el entorno virtual en linux y MacOs
deactivate -> desactivamos el entrono virtual

pip freeze -> muestra los modulos instalados en el entorno virtual
pip install paquete -> instalamos un modulo o paquete
pip freeze > requirements.txt -> mandamos a un archivo de texto plano los paquetes intalados, asi se pueden compartir
pip install -r requirements.txt -> instalamos los paquetes que estan en el archivo de paquetes

** List comprehensions **

> > > se utiliza para generar nuevas listas

[elemento for elemento in iterable if condicion] -> sintaxis de una list comprehensions

** Diccionarios comprehensions **

> > > se utiliza para generar nuevos diccionarios

{llave:valor for elemento in iterable if condicion} -> sintaxis para un diccionario comprehensions

** funciones anonimas / lambdas **

> > > son funciones sin nombre (no tienen un identificador), puede tener los argumantos que necesites, pero solo en una linea de codigo es decir una sola expresión

variable = lambda argumentos: expresion

** Funciones de orden superior **

> > > reciben como parametros otras funciones

== filter ==

> > > rebibe dos parametros, una funcion y un parametro iterable, esto retorna un iterados
> > > variable = list( filter( lambda, list ) )

== map ==

> > > rebibe dos parametros, una funcion y un parametro iterable
> > > variable = list( map( lambda, list ) )

== reduce ==

> > > rebibe dos parametros, una funcion y un parametro iterable
> > > se tiene que importar de functools

variable = reduce( lambda, list )

** EXEPCIONES **

> > > se utiizan para no generar errores y terminar el programa tan abuptamente

raise TipoError('mensaje') -> se maneja un error que sabemos que esta mal pero no ejecuta un error explicito

try:

    raise TipoError('mensaje')
    bloque de codigo

except TipoError as alias_error:
bloque de codigo

try:
bloque de codigo
except TipoError:
bloque de codigo
else:
bloque de codigo

try:
bloque de codigo
except TipoError:
bloque de codigo
finally:
bloque de codigo

=== assert ===

assert condicion , mensaje de error -> si no se cumple la condicion muestra el mensaje de error, una forma más de cachar los errores, reducioendo en algunas ocaciones el try-except

** Scope **
z:int = 2 -> global scope

def run():
z:int = 1 -> local scope

** Closures **
Las variables de orden superior son recordadas por ordenes inferiores

** Decoradores **
Funcion que recibe como parametro otra funcion y le añade cosas y retorna uan funcion diferente

    				***** POO *****

Los objetos en python tienen propiedades y metodos

=>Clases
se utiliza la palabra reservada (class)

->class Nombre_clase:
atributos = valor

Llamada de la clase

    -> instancia = Nombre_clase()

para acceder a las propiedades de la clase
-> instancia.atributo

=> clases mejoradas

class nombreClase:
def **init**(self, atributo1, atributo2, ...):
self.atributo1 = atrubuto1
self.atributo2 = atrubuto2

se utiliza la palbra reservada (**init**) que sera ejecutado siempre al primer metodo que se ejecuta
al igual que la palabra reservada self que hara referencia al objeto/instancia

    				***** HERENCIA *****

para hacer referencia a que una clase tiene herencia se utiliza la siguiente sintaxis

class combreClase(nombreClasePadre):
atributos y metodos
//def atributo(instancia)

La clase padre no pueden acceder a los metodos ni atributos
P/e:
class Animal:
def **init**(self, nombre, onomatopeya):
self.nombre = nombre
self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola! soy un ', self.tipo , ' y mi sonido es ', self.onomatopeya)

class Gato(Animal):
tipo = 'gato'

class Perro(Animal):
tipo = 'perro'

gato=Gato('pelusa', 'maullido')
perro=Perro('wifi', 'ladrido')

gato.saludo()
perro.saludo()

    				***** MODULOS *****

=>import nombreArchivo

llamda de atributos
=>nombreArchivo.atributo

*Renombrar modulos se utiliza la palabra reservada AS
->import nombreModulo as nuevoNombre
*importar datos metodos especificos
->from nombreModulo import metodos/variables, otrosModulos

    				***** ARCHIVOS *****

\*Abrir un archivo se utiliza la palabra reservada Open()
variable = open('nombre_archivo')

\*Para leer un archivo completamente
print(varicale.read())

\*Para leer linea por linea
print(varicale.readline())

permisos para abrir un archivo en python
variable = open('nombre_archivo', persimos)

'r' -> read
'a' -> append (agraga texto sin remplazar)
'w' -> writhe (remplaza todo lo del archivo, en caso de que no exista lo crea)
'x' -> crea el archivo, si ya existe manda un error

una vez leido el archivo lo cerramos
variable.close()

\*Agregar texto al archivo
variable = open('nombre_archivo', 'a') -> agragar texto
variable.write('texto') -> cambia todo el texto y se necesita abrir otra vez el archivo

\*Eliminar archivos
se utiliza un modulo
import os

os.remove('nombre_archivo')

validar si el archivo existe o no
if os.path.exists('nombre_archivo')
os.remove('nombre_archivo')
else
print('el archivo no existe')

\*Para eliminar un directorio
os.rmdir('ubicacion_archivo')
