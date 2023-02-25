# GIT AND GITHUB

saber la version de Git que se tiene 
```
git --version
```

---
## Configurar entorno local
---
#### se requiere configurar para que el repositorio sepa quien esta haciendo los cambios

muestra toda la configuracion del entrono
```
git config
```
muestra la configuracion por defecto
```
git config --list
```
muestra la configuracion del respositorio 
```
git config --list --show-origin
```
muestra la configuracion global y se puede modificar las variables
```
git config --global -e
```
agrega un usuario
```
git config --global user.name <"name">
```
agregar un correo al usuario o cambiar el email
```
git config --global user.email <"email">
```
cambiar el nombre de la rama por default cuando se crea el repo "master -> main" desde la configuracion local
```
git config --global init.defaultBranch <name>
```
se crea un alias de los comandos, de forma personalizada
```
git config --global alias.<tu-comando> <comando>
```
si el comando tiene espacios se debe de poner entre comillas dobles el comando
```
git config --global alias.<tu-comando> <"comando">
```
corregir warning de saltos de linea en windows
```
git config core.autocrlf true
```

---

## Comandos

---

inicia un repositorio, para que los archivos puedan tener un historial
```
git init
```

## Estatus

conocer el estatus de los archivo
- U = Sin seguimiento
- M = Modificado
- D = Eliminado
- A = Agregado

```
git status
```

muestra de forma breve el estado del archivo
```
git status --short
```

## Agregar un archivo al staging

agregar un archivo al repositorio
```
git add <archivo>
```

agregar todos los archivos modificados al respositorio
```
git add .
```

agregar una carpeta con sus archivos
```
git add <carpeta>
```

agregar un archivo de cierta carpeta
```
git add <carpeta/archivo.extencion>
```

## Eliminar un archivo del staging

remover un archivo del repositorio
```
git rm <archivo>
```

remover un archivo de cache
- \--cached = vuelve al estado inicial fuera del status
```
git rm --cached <archivo>
```

remover un directorio con archivos dentro, solo del respositorio local
- \-r = recursiva
```
git rm --cached -r <directorio>
```

elimina los archivos de git y del disco duro
- \--force = de forma forsada
```
git rm --force <archivo>
```

## Commit

agregar un comentario de los cambios realizados
```
git commit -m <mensaje>
```
hace el commit y el add de los cambios (solo si ya estan agregados los archivos previamente)
```
git commit -am <mensaje>
```
se cambia el comentario del commit anterior abriendo un editor
```
git commit --amend
```
se cambia el comentario sin abrir el editor
```
git commit --amend -m <mensaje>
```

## Log

ver historia del repositorio
```
git log
```

muestra toda la historia del archivo
```
git log <archivo>
```

se muestran los combios en la consola junto a los logs
```
git log --stat
```

mustra todo lo que ha ocurrido en todo el repositorio y ramas
```
git log --all
```

muestra la historia con algunos detalles visuales de como se han fucionado las ramas
```
git log --all --graph
```

muestra como se han fucionado las ramas de forma más presisa
```
git log --all --graph --decorate --oneline
```

se muestra de forma corta el commit, solo con el hashcommit y la descripcion
```
git log --oneline
```

buscamos la palabra en los commits realizados
```
git log -S "palabra"
```

## Show

muestra los cambios que se hicieron en el archivo
```
git show <archivo>
```

muestra las ramas que existen y su historia
```
git show-branch
```

muestra toda la historia de la rama
```
git show-branch --all
```

## Diferencias
muestra la comparativa entre los dos archivos (influye el orden de los commits)
```
git diff <commitA> <commitB>
```
muestra la comparativa pero de los cambios en staged
```
git diff --staged <commitA> <commitB>
```

## Reset

elimina un archivo del stach
```
git reset <archivo>
```

revertir cambios
```
git reset <version>
```

revertir cambios sin imporatar que haga
```
git reset <version> --hard
```

revertir cambios pero los anteriores archivos agregados se mantienen
```
git reset <version> --soft
```

sacamos los archivos de memoria pero no se borran y se tienen que agregar de nuevo
```
git reset HEAD
```

movernos un commit antes de HEAD, para agregar cambios olvidados
```
git reset --soft HEAD^
```

hacer que la rama remota sea el nuevo HEAD quitando todos los cambios
```
git reset --hard origin/<rama>
```

saca todos los commits realizados posteriormente y los pone en el staged
```
git reset --mixed <hascommit>
```

revierte todos los cambios hasta ese hash commit
```
git reset --hard <hashcommit>
```

muestra toda la historia que se realizo en el repositorio - obsolutamente toda la historia
```
git reflog
```

## Checkout

traer cambios hechos por otra persona en una rama
```
git checkout
```

reconstruye todos los archivos segun el ultimo commit
```
git checkout -- .
```

cambiamos de rama 
- si no se hace add y commit, cuando se cambia de rama se pierde todo lo modificado
```
git checkout <nombre_rama>
```

crea una rama y hace checkout de la rama
```
git checkout -b <nombre_rama>
```

regresa un archivo al commit solicitado
```
git checkout commit <archivo>
```

regresamos a la ultima version
```
git checkout master <archivo>
```

## Branch

muestra todas las ramas locales y la rama en la que estamos trabajando
```
git branch
```

cambiar el nombre de una rama
```
git branch -m <rama> <nombre>
```

creamos una rama
```
git branch <nombre-rama>
```

eliminamos un rama
```
git branch -D <nombre-rama>
```

eliminamos una rama sin importar nada
```
git branch -d <nombre-rama> -f
```

nos muestra las ramas remotas
```
git branch -r
```

nos muestra todas las ramas tanto remotas como locales
```
git branch -a
```

## Clonar un repositorio

clonamos todo lo que esta en el repositorio remoto
```
git clone <url> 
```

## Pull and fetch

nos indica si existen cambios en el repositorio remoto y los baja
```
git fetch
```

traemos y actualizamos nuestros archivos
```
git pull
```

forzar a fucionar cambios del repositorio con nuestro local
```
git pull origin <rama> --allow-unrelated-histories
```



## Push

se manda el head al servidor remoto
```
git push
```

mandamos al repositorio remoto nuestra rama local
```
git push origin <nombre-rama>
```

eliminar ramas remotas
```
git push origin --delete <nombre-rama>
```


## Stash
#### guardar los cambios de forma temporal sin hacer push

agregar cambios a un entorno temporal
```
git stash
```

muestra los stash guardados temporalmente
```
git stash list
```

regresar los cambios del stash
```
git stash pop
```

colocar el stash en un rama
```
git stash branch <nombre-rama>
```

borrar los stash
```
git stash drop <index>
```

## Gitk and gitkeep

interfas de git local
- gitk

se crea este archivo para los direcctorios vacios y puedan ser tomados en cuenta por git
- .gitkeep


## Merge
#### cambiar a la rama master ya que es la rama principal antes de hacer un merge

fucionar las versiones que se bajaron con el fetch
```
git merge
```

fucionamos las ramas y se debe agrega un mensaje
```
git merge <rama> <mensaje>
```


## Conflictos
> - se hace un merge y mostrara los errores de las lineas que son afectadas
> - se puede eliminar las lineas que generen el error de forma manual, posteriormente se debe realizar un commit despues de solucionar los conflictos

## Remote
> Conectar con repositorio remoto

lista el repositorio remoto al que apunta
```
git remote
```

muestra el origin para hacer push y fetch
```
git remote -v
```

agrega el repositorio
```
git remote add origin <url>
```

cambiar la url del repositorio remoto
```
git remote set-url origin <url>
```

agregamos un repositorio nuevo de donde hacer pull y push
```
git remote add upstream <url>
```

## SSH
> Creacion de llaves SSH

crear una llave ssh en la carpeta .ssh/id_rsa
```
ssh-keygen -t rsa -b 4096 -C <correo-git>
```

evaluando si rdts corriendo el agente de ssh y se ejecuta de manera correcta
```
eval $(ssh-agent -s)
```

se agrega la llave privada al ssh
```
ssh-add <ruta-llave-privada>
```

## Tags

Tags
git tag -a name -m "mensaje" hash_commit            -> agregamos una etiqueta
git tag                                             -> vemos todas las tags
git show-ref --tags                                 -> vemos la tag y el hash del commit asignado
git push origin --tags                              -> mandamos los tags al repositorio remoto
git tag -d name_tag                                 -> eliminar una tag de forma local
git push origin :refs/tags/name_tag                 -> elimina la referencia del tag en el repositorio remoto


## Fork
> - se clona el proyecto como un fork y podemos modificar ya que es un clonado del mismo, para poder hacer cambios se debe hacer un pull request
> - funcionan de la misma manera que las ramas
> - siempre que se desee ver los cambios que hay se hacer un pull ya que los forks se quedan y no se actualizan solos


## Rebase
> - estando en la rama creada se ejecuta el comando rebase, primero se hace el rebase a la rama que se desaparecera de la historia
> - despues se le hace rebase a la rama principal

git rebase master                                   -> paga los cambios de otra rama a la rama indicada / reescribe la historia del repositorio


## Clean
> - no actua sobre archivo de -gitignore
> - no actual sobre directorios

git clean --dry-run                                 -> mustra los archivo que se borraran
git clean -f                                        -> se borraon lo archivo


## Cherry-pick
git cherry-pick hash_commit                         -> traer un commit de una rama al master (cuando aun no se termina)


## Hacer busquedas
git grep "palabra"                                  -> buscamos la palabra en todo nuestro versionador
git grep -n "palabra"                               -> buscamos y nos dice en que linea y archivo se encuentra la palabra
git grep -c "palabra"                               -> saber cuantas veces uso la palabra en todo el repositorio

git short log -sn                                   -> muestra las personas que han hecho ciertos commits
git short log -an --all                             -> muestra todos los commits aunque sean borrados
git short log -an --all --no-merges                 -> no incluye los merges que se realizaon 

git blame nombre_archivo                            -> se muestra liena por linea para saber quien modifico el archivo
git blame -c nombre_archivo                         -> se muestra liena por linea pero mas identado para saber quien modifico el archivo
git blame archivo -L10,60                           -> muestra quien ha hecho cambios entre las lineas indicadas por -L
git blame --help                                    -> muestra un manual de los comandos
