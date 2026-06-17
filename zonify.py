from flask import Flask, render_template, redirect, url_for #El flask es lo que deja crear el servidor web, el render template es lo que comina los archivos html y combinarlos con los datos que recibe python para mostrarlos bien al usuario y el redirect y el urlfor sirven para que si pasa un evento, lo mande rapido a la pagina.
from services.cosevi_service import obtener_eventos_cosevi #esta linea hace que del codigo de cosevi service, generado junto al api publico de cosevi y ayuda de ia, jale la definicion que se usa para otener los datos de la api 

app = Flask(__name__) #basicamente esta linea sirve para que el servidor web exista
eventos_cache = [] #Es una lista vacia en la RAM que es para guardar datos temporalmente y hacer la web mas rapida

@app.route("/") #apenas el usuario entre, esto hace que se ejecute la funcion de inicio, la cual tiene que ver con lo que ve el usuario en el html
def inicio():
    global eventos_cache #Le avisa a python que vamos a usar la lista creada anterior mente al ejecutar la funcion

    if not eventos_cache: #Esta linea lo que hace es preguntar si la lista esta vacia o no, si la respuesta es si va, y jala la funcion de obtener datos cosevi
        eventos_cache = obtener_eventos_cosevi()

    return render_template( # Esto es lo que hace que se le muestre al usuario. Toma html y le manda la lista de accidentes que tenemos guardada o de la api de cosevi 
        "index.html",
        eventos=eventos_cache
    )


@app.route("/actualizar") #Basicamente esto sirve para actualizar los datos una vez el usuario ya lleva cierto tiempo en la pagina
def actualizar():
    global eventos_cache

    eventos_cache = obtener_eventos_cosevi()

    return redirect(url_for("inicio"))


if __name__ == "__main__": #Esto es lo que enciende el saervidor, que hace que solo arranque la web si se ejecuto el archivo desde la terminal
    app.run(debug=True)