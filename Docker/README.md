# Docker

## Modulo Uno - Primeros pasos

### Comandos basicos

Obtener ayuda de un comando
```
docker <comando> --help
```

Descargar una imagen del repositorio de DockerHub
```
docker pull IMAGE_NAME
docker pull IMAGE_NAME:TAG

ejemplo:
docker pull postgres
docker pull postgres:15.1
```

Correr un contenedor:
- \-d = Corre la imagen desenlazada de la consola donde se ejecutó el comando
- \-p = Especificar un puerto, (puerto de la computadora : puerto del conetenedor)
- name = nombre de la imagen a usar
```
docker container run -d -p 80:80 IMAGE_NAME

ejemplo:
docker container run -d -p 80:80 docker/getting-started
```

## Glosario de Términos

* Docker
	* Docker es una herramienta diseñada para facilitar la creación, la implementación y ejecucion de aplicaciones mediante el uso de contenedores.
* Container - Contenedor
	* Es una instancia de una imagen ejecutándose en un ambiente aislado.
* Image - Imagen de contenedor
	* Es un archivo construido por capas, que contiene todas las dependencias para ejecutarse, tal como:
		* las dependencias
		* configuraciones
		* scripts
		* archivos binarios