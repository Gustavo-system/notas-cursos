# primer paso instalamos la libreria de Flask y la importamos en nuestra aplicion
from flask import Flask

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
@app.route('/usuario/<str:nombre>') # se definen los parametros que se reciben y se le agrega el tipo para forzar que asi sea
def usuario(nombre):
    return 'El nombre es ' + nombre