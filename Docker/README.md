# Docker

## Modulo Uno - Primeros pasos

\
Obtener ayuda de un comando

```
docker <comando> --help
```

---

## Imagenes

---

Descargar una imagen del repositorio de DockerHub

```
docker pull IMAGE_NAME
docker pull IMAGE_NAME:TAG

ejemplo:
- docker pull postgres
- docker pull postgres:15.1
```

Mostrar todas las imagenes descargadas

```
docker images

docker image ls
```

Borrar una o mas imagenes

```
docker image rm <image-ID> o <ID1 ID2 ID3…>

docker rmi name_imagen
```

Borrar todas las imagenes sin importar nada

```
docker image prune
```

Borrar todas las imágenes no usadas

```
docker image prune -a
```

---

## Contenedores

---

Mostrar un listado de todos los contenedores corriendo en el equipo

```
docker container ls

docker ps
```

Mostar todos los contenedores que esten corriendo o no esten corriendo

```
docker container ls -a
```

Correr un contenedor:

-   \-d = Corre la imagen desenlazada de la consola donde se ejecutó el comando
-   \-p = Especificar un puerto, (puerto de la computadora : puerto del conetenedor)
-   IMAGE_NAME = nombre de la imagen a usar

```
docker container run -d -p 80:80 IMAGE_NAME

ejemplo:
docker container run -d -p 80:80 docker/getting-started
```

Iniciar un contenedor previamente creado

```
docker container start <container-id>
```

Asignar un nombre al contenedor

```
docker container run --name myName IMAGE_NAME
```

Detener un contenedor

```
docker container stop <container-id>
```

Detener contenedores y removerlos de forma forzada

```
docker container rm -f <container-id> o <ID1 ID2…>
```

Borrar contenedores

```
docker container rm <container-id>
```

Borrar todos los contenedores detenidos

```
docker container prune
```

---

## Glosario de Términos

---

-   Docker
    -   Docker es una herramienta diseñada para facilitar la creación, la implementación y ejecucion de aplicaciones mediante el uso de contenedores.
-   Container - Contenedor
    -   Es una instancia de una imagen ejecutándose en un ambiente aislado.
-   Image - Imagen de contenedor
    -   Es un archivo construido por capas, que contiene todas las dependencias para ejecutarse, tal como:
        -   las dependencias
        -   configuraciones
        -   scripts
        -   archivos binarios
