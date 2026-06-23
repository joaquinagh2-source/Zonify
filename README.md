# Zonify
En Este proyecto lo que se realizo o se intento realizar es un sistema web que permita ver los accidentes, averias, cortes de luz,etc, en tiempo real de Costa Rica con datos reales.

# Que Hicimos?
1. Intentamos Conectar Python con el API oficial de COSEVI para descargar los accidentes mas recientes en las calles del pais, y tambien lo intentamos con un end point encontrado en una pagina oficial de la CNFL sin embargo, debido a que no nos daba realmente la informacion en vivo, decidimos cambiarlo por un archivo csv que es como una hoja de calculo, para que sea como una base de datos propias de sucesos en costa rica, asi no tenemos que estar buscando apis que se actualizen o que tengan datos reales ya que lo podemos hacer nostros.

2. Un HTML con CSS limpio para que se muestren de manera detallada y entendible los sucesos en Costa Rica, tanto como de luz, agua, accidentes y trafico de momento con informacion puesta en nuestra hoja de caclulo, pero a futuro con datos reales en vivo.

3. Intentamos colocar un filtro por ubicacion en JavaScript y Python, que lo que se espera que haga es que a la hora de que un usuario ingrese a la app web, se detecte en donde esta ubicado usando la biblioteca llamada geopy, para poder filtrar los resultados dependiendo de esa ubbicacion, o almenos esa es la idea que teniamos, a pesar de que no nos ha funcionado muy bien por ciertas dificultades.

# Dificultades

1. El primer obstaculo que tuvimos a la hora de empezar el proyecto, fue darnos cuenta que la idea original del mapa realmente no nos iba a funcionar debido a falta de tiempo y de conocimientos sobre el tema. Intetamos crear un mapa con la herramienta leaflet, pero conectarlo era muy complicado por lo que decidimos hacer simplemente una pagina que mostrara los acontecimientos.

2. Luego tuvimos que cambiar la dinamica ya qque nos dimos cuentas que las apis y servicios que habiamos conseguido no nos daba la informacion correcta y aparte no se actualizaba en tiempo real(COSEVI y CNFL). 

3. A la hora de implementar la geolocaclizacion tuvimos problema ya que el no estaba funcionando de la manera que queriamos, por lo que tuvimos que quitar la biblioteca de geopy y el codigo realizado.

# REQUISITOS PREVIOS
1. Antes de ejecutar la app, hay que tener instalado Python3 en el sistema operativo si o si, accediendo a esta pagina https://www.python.org/downloads/.

2. Tambien para trabajar en este proyecto, hay que descargar las bibliotecas necesarias, para esto tenemos el archivo requirements.txt, que tiene las bibliotecas y sus versiones.
Para instalarlas se ocupa ejecutar el comando **pip install -r requirements.txt** esto lo que hara es descargar todas las librerias externas de python.

3. En caso de que se quiera hacer automatico, hay que encontrar un api que sirva en tiempo real lo cual es complicado de encontrar, o tener un archivo CSV(hoja de calculo) con la informacion que quieras colocar en la pagina, en nuestro caso tenemos **Accidentes.csv**, es un tipo de base de datos propia que a la hora de colocar averias, se veran en la pagina.

# Estructura del Código 
1. **Lectura y Limpieza:** El archivo se abre en modo lecutra que es **mode=r** con codificación **utf-8** para evitar problemas con las tildes y caracteres de Costa Rica ya que sin esto puede llegar a generar ciertos errores.Aparte, se usa **csv.DictReader** para que cada fila de nuestro archivo en el que se va a almacenar toda la informacion de los accidentes pueda ser leida de y proyectada en nuestra pagina web.

2. **Clasificación Automática:** Un ciclo **for** evalúa cada fila, pasa las descripciones a mayúsculas con la etiqueta **.upper()** para evitar fallos y añade los elementos con **.append()** a sus listas **averias_cnfl, cortes_aya ,eventos_cosevi** para ser mostradas a la hora de que la app empiece a funcionar **@app.route("/")**.

3. **Diseño**: El diseño de la pagina esta realizado con **HTML** y **CSS** siguiendo una estructura minimalista y con una interfaz facil de entender para el usuario a la hora de ingresar. Tambien con ayuda de **JavaScript** colocamos un filtrador para poder buscar segun la provincia, asi las personas pueden buscar accidentes cerca de su casa. 

# Recomendaciones para continuar el proyecto

1. Continuar con la implementacion de leaflet: Crear un mapa en leaflet es muy sencillo, hay tutoriales en la misma pagina o en youtube que permiten hacer que el mapa sea interactivo, y puede que haya una manera de adaptar el codigo a mapa para que se puedan ver los acontecimientos en el mapa interactivo.

2. Buscar APIS: almenos en Costa Rica hay pocas APIS publicas que sirven, pero las privadas fijo si. Si se piensa emoezar a desarrollar la idea de manera profesional, a lo mejor y se pueden buscar en municipalidades, pidiendo permisos a empresas como la CNFL como desarrollador u otras maneras de conseguir estas APIS.

3. Mucha paciencia: Para realizar este proyecto se ocupan bastantes conocimientos en programacion, tanto en html, css, js, python, y github, y al principio puede parecer confuso, pero estrcturando bien los pasos se puede sacar un proyecto bastante bonito. No es algo que se logre en una sola semana, se ocupa bastante dedicacion y tiempo para lograrlo.








