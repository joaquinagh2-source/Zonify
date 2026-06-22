# Zonify
En Este proyecto lo que se realizo o se intento realizar es un sistema web que permita ver los accidentes, averias, cortes de luz,etc, en tiempo real de Costa Rica con datos reales

Que Hicimos?
1. Intentamos Conectar Python con el API oficial de COSEVI para descargar los accidentes mas recientes en las calles del pais, y tambien lo intentamos con un end point encontrado en una pagina oficial de la CNFL sin embargo, debido a que no nos daba realmente la informacion en vivo, decidimos cambiarlo por un archivo csv que es como una hoja de calculo, para que sea como una base de datos propias de sucesos en costa rica, asi no tenemos que estar buscando apis que se actualizen o que tengan datos reales ya que lo podemos hacer nostros

2. Un HTML con CSS limpio para que se muestren de manera detallada y entendible los sucesos en Costa Rica, tanto como de luz, agua, accidentes y trafico de momento con informacion puesta en nuestra hoja de caclulo, pero a futuro con datos reales en vivo

3. Intentamos colocar un filtro por ubicacion en JavaScript y Python, que lo que se espera que haga es que a la hora de que un usuario ingrese a la app web, se detecte en donde esta ubicado usando la biblioteca llamada geopy, para poder filtrar los resultados dependiendo de esa ubbicacion, o almenos esa es la idea que teniamos, a pesar de que no nos ha funcionado muy bien por ciertas dificultades.

# REQUISITOS PREVIOS
Antes de ejecutar la app, hay que tener instalado Python3 en el sistema operativo si o si
