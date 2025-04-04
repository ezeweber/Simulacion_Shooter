En este repositorio se plantea un programa que procesa una partida de una juego shooter online, dado un conjunto de rondas con sus resultados. En base a los resultados de cada ronda se aplica el siguiente sistema de puntuación por jugador: Por kill suma 3 puntos, por asistencia 1 y si murió esa ronda resta 1.
Este programa para que pueda abrirse y ejecutarse correctamente, debe instalar algunas dependecias para lo cual es recomendable usar un entorno virtual. 

<!-- Este procesamiento y el registro de rondas se encuentra en la carpeta notebooks, en el archivo main que es de tipo ipynb.  -->

¿QUE ES UN ENTORNO VIRTUAL?

Un entorno virtual es una carpeta donde almacena funcionalidades y las librerias necesarias para correr el programa, sin afectar el resto del sistema. Para hacer uso de este y visualizarlo de manera correcta, deberá instalar en su computadora un editor de texto, tal como visual studio code, y el lenguaje de programacion python. Luego volviendo a este repositorio donde dice (<>code) resaltado en color verde hay una opcion de descargar el proyecto en un .zip y descomprimirlo. 

EJECUTANDO EL PROGRAMA

Luego de instalar vs code y python, abrir la aplicacion visual studio code y en file abrir la carpeta descomprimida del proyecto. Antes de visualizar las carpetas y sus contenidos debemos crear un entorno virtual para correr el programa luego. Para ello por medio del comando de teclado: CONTROL(ctrl) + SHIFT(flecha hacia arriba) + P (PULSAR AL MISMO TIEMPO) Esto abrira una ventana de busqueda donde pondremos: Create new Terminal y pulsamos enter. En esta terminal que abrimos copiar y pegar esta linea a ejecutar:

python -m venv venv

Esto creara una carpeta donde vamos a almacenar las librerias necesarias para visualizar el programa. Una vez creada se ACTIVA con el siguiente comando en la terminal:

(si su sistema operativo es windows) 
venv/Scripts/activate
(si es linux o mac)
venv/bin/activate

Y para desactivarlo: (una vez ya probado el programa y antes de cerrar todo, se recomienda hacerlo)

venv/Scripts/deactivate o venv/bin/deactivate

REQUIREMENTS

Entre los archivos se encuentra requirements(requerimientos) a instalar para que todo funcione correctamente dentro de nuestro entorno virtual creado. Para esto en consola se debe escribir lo siguiente

pip install requirements.txt

EJECUCION DEL PROGRAMA

Ahora si, de estar todo instalado de manera apropiada podrá abrir el archivo main.ipynb que se encuentra en la carpeta notebooks. Se le abrira una ventana con el programa y vera texto indicando que se realizará, intercalado con recuadros de codigo. A medida que vaya leyendo el documento, donde aparezca codigo tendrá que ejecutar con el "boton" de play que aparece arriba a la izquierda, en cada uno de los recuadros. 

Espero que mi proyecto sea de su agrado!