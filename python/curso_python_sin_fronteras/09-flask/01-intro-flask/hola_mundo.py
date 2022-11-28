# primer paso instalamos la libreria de Flask y la importamos en nuestra aplicion
from flask import Flask, request

# incializamos la aplicacion y creamos nuestro primer recurso
app = Flask(__name__)

# primer recurso
@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/lala')
def lala():
    return 'lala'

# como tercer paso debemos indicarle a Flask en donde esta nuestra app en la linea de comandos
# export FLASK_APP=archivo.py o en windows en powershel set FLASK_APP=archivo.py

# levantamos nuestro servidor con el comando 
# flask run

# avilitamos el entorno de desarollo para que nuestra app recargue cada que detecte un cambio
# export FLASK_ENV=development o en windows set FLASK_ENV=development

# Recursos con variables en las rutas
@app.route('/usuario/<nombre>') # se definen los parametros que se reciben y se le agrega el tipo para forzar que asi sea
def usuario(nombre):
    return 'El nombre es ' + nombre


# metodos HTTP
# GET, POST, PUT, PATCH, DELETE
@app.route('/usuario2', methods=['GET', 'POST']) # se indican los metodos por el cual se podra acceder a este recurso
def usuarios2():
    # podemos realizar una consulta por medio de la consola usando curl
    # curl -X HTTP_METHOD URL
    # curl -X GET http://localhost:5000/usuarios2
    return 'metodos HTPP'


# se puede separar la logica de cada metodo HTTP en funciones distintas o se puede hacer en una sola por medio del objeto request que se importa desde flask
@app.route('/inventario', methods=['GET', 'POST']) # si a una ruta no se le indican los metodos, esta tiene por default GET
def inventario():
    if request.method == 'GET':
        return 'preticion por el metodo GET'
    else:
        return 'peticion por el metodo POST'