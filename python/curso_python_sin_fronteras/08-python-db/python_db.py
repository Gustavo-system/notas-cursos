"""
Para hacer uso de mysql con python se debe instalar la libreria de 
- mysql-connector-python    -> esta para versiones 8+ de mysql
- mysql-connector           -> para versiones como la 5 de mysql

la forma de instalarlo es la siguiente
- pip install mysql-connector-python

En mac o sistemas linux
- pip3 install mysql-connector-python

Se puede agregar al archivo de requirements.txt el nombre de la libreria en caso que se este usando un entorno virtual
"""

import mysql.connector

# obtenemos una instancia de la base de datos
my_db = mysql.connector.connect(
    host='localhost',
    user='your_user',
    password='your_password',
    database='name_db'
)

# por medio del cursos podemos manipular las operaciones de la base de datos
cursor = my_db.cursor()


# sintaxis de las consultas utilizando el cursos
# cursor.execute(query)

# obtener todos los registros de una tabla
cursor.execute('select * from db_inventarios.tc_aplicaciones')
resultado = cursor.fetchall()
print(resultado)


# obtener un solo registro
resultado = cursor.fetchone()
print(resultado)


# insertar datos
# es necesario crear una variable con la consulta sql
query_sql = 'insert into Tabla (columna1, columna2, columna3) values (%s, %s, %s)'
# se crea la variable values y se le asigna un set con los valores a ingresar en el query
values = ('valor1', 'valor2', 'valor3')
# ejecutamos la consulta, pasando dos paramentos, la query y los valores
cursor.execute(query_sql, values)
# hacemos que los valores se guaren en la base de datos
my_db.commit()
# mostramos el rowcount que indica el numero de filas afectadas con la ejecucion de la consulta, la cual deberia devolver 1
print(cursor.rowcount)
# ya podemos consultar los datos como en el ejemplo anterior y se deben mostrar registrados en la base de datos


# actualizar datos
query_sql = 'update Table set columna = %s where id = %s'
values = ('valor1', 'valor2')
cursor.execute(query_sql, values)
my_db.commit()
print(cursor.rowcount)


# eliminar registros
query_sql = 'delete from Tabla where id = %s'
values = (1, ) # Es importante saber que se debe dejar un espacio despues de la coma para que se ejecute de forma correcta la query
cursor.execute(query_sql, values)
my_db.commit()
print(cursor.rowcount)