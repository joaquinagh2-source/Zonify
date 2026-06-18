from flask import Flask, render_template, redirect, url_for, request #El flask es lo que deja crear el servidor web, el render template es lo que comina los archivos html y combinarlos con los datos que recibe python para mostrarlos bien al usuario y el redirect y el urlfor sirven para que si pasa un evento, lo mande rapido a la pagina.
from services.cosevi_service import obtener_eventos_cosevi #esta linea hace que del codigo de cosevi service, generado junto al api publico de cosevi y ayuda de ia, jale la definicion que se usa para otener los datos de la api 
from services.cnfl_averias_service import obtener_averias_cnfl
from geopy.geocoders import Nominatim

app = Flask(__name__) #basicamente esta linea sirve para que el servidor web exista
eventos_cache = [] #Es una lista vacia en la RAM que es para guardar datos temporalmente y hacer la web mas rapida
averias_cache = []


@app.route("/") #apenas el usuario entre, esto hace que se ejecute la funcion de inicio, la cual tiene que ver con lo que ve el usuario en el html
def inicio():
    global eventos_cache #Le avisa a python que vamos a usar la lista creada anterior mente al ejecutar la funcion
    global averias_cache

    if not eventos_cache: #Esta linea lo que hace es preguntar si la lista esta vacia o no, si la respuesta es si va, y jala la funcion de obtener datos y averias
        eventos_cache = obtener_eventos_cosevi()
    if not averias_cache:
        averias_cache = obtener_averias_cnfl()

    clientes_afectados = sum
    (averia.get("clientes_afectados") or 0 
    for averia in averias_cache) #Esta linea hace una suma de todos los clientes afectados por las averias, para mostrarlo en el html




    return render_template( # Esto es lo que hace que se le muestre al usuario. Toma html y le manda la lista de accidentes y averias que tenemos guardada  
        "index.html",
        eventos=eventos_cache
    )

    return render_template(
        "index.html",
        averias=averias_cache,
        clientes_afectados=clientes_afectados,
    )


@app.route("/actualizar") #Basicamente esto sirve para actualizar los datos una vez el usuario ya lleva cierto tiempo en la pagina
def actualizar():
    global eventos_cache
    global averias_cache

    eventos_cache = obtener_eventos_cosevi() 

    try:#Verificar si funciona y si no, mostrar error pero sin que se caiga la pagina
        averias_cache = obtener_averias_cnfl()
    except RuntimeError as e:
        averias_cache = []
        print("Error al actualizar averias de CNFL:", e)

    return redirect(url_for("inicio"))




@app.route("/ubicacion")
def detectar_provincia():
    #Aqui agarramos las cordenadas del ususario
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return redirect(url_for("inicio"))#Esto es para que si falla lo mande al inicio normal

    try:
        geolocator = Nominatim(user_agent="zonify_cr")# Esto basicamente es un traductor de cordenadas que hace que se pueda ubicar donde se encuentra el usuario en base a esas cordenadas
        ubicacion_completa = geolocator.reverse(f"{lat}, {lon}")

        direccion = ubicacion_completa.raw.get("address", {})#Extramos la provincia que se consiguieron con la traduccion
        provincia_detectada = direccion.get("state", "No disponible")

        global eventos_cache #Filtramos los eventos de nuestra caché usando la provincia
        if not eventos_cache:
            eventos_cache = obtener_eventos_cosevi()


        eventos_filtrados = [] #Esto limpia el texto para que coincida con el formato del API de  COSEVI
        for evento in eventos_cache:

            if evento ["provincia"].lower() in provincia_detectada.lower(): #Si la provincia del usuario, coincide con la del evento se agrega a la lista de los eventos
                eventos_filtrados.append(evento)

        if eventos_filtrados:   #Si hay accidentes en esta provincia los mostramos de primeros
            return render_template("index.html", eventos=eventos_filtrados, provincia=provincia_detectada)

    except Exception as e:#En caso de error redireccionar al arranque de inicio
        print("Error detectando ubicacion", e)

    return redirect(url_for("inicio"))

if __name__ == "__main__": #Esto es lo que enciende el saervidor, que hace que solo arranque la web si se ejecuto el archivo desde la terminal
    app.run(debug=True)