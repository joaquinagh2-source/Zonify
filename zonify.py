from flask import Flask, render_template, redirect, url_for, request #El flask es lo que deja crear el servidor web, el render template es lo que comina los archivos html y combinarlos con los datos que recibe python para mostrarlos bien al usuario y el redirect y el urlfor sirven para que si pasa un evento, lo mande rapido a la pagina.
from geopy.geocoders import Nominatim
import csv
import os


app = Flask(__name__) #basicamente esta linea sirve para que el servidor web exista
accidentes_cache = [] #Es una lista vacia en la RAM que es para guardar datos temporalmente y hacer la web mas rapida

COORDENADAS_PROVINCIAS = {
    "San José": {"lat": 9.9333, "lon": -84.0833},
    "Alajuela": {"lat": 10.0167, "lon": -84.2167},
    "Cartago": {"lat": 9.8644, "lon": -83.9194},
    "Heredia": {"lat": 10.0024, "lon": -84.1165},
    "Guanacaste": {"lat": 10.6333, "lon": -85.4333},
    "Puntarenas": {"lat": 9.9763, "lon": -84.8384},
    "Limón": {"lat": 10.0022, "lon": -83.0446}
}

def leer_Accidentes_csv():
    lista_accidentes = []
    archivo_ruta = "accidentes.csv"

    # Verificar si el archivo existe antes de intentar abrirlo
    if not os.path.isfile(archivo_ruta):
        print(f"ERROR: No se encontro el archivo {archivo_ruta}")
        return []

    try:
        with open(archivo_ruta, mode="r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                provincia = fila.get("provincia", "").strip()

                coordenadas = COORDENADAS_PROVINCIAS.get(provincia)

                Accidente = {
                    "id": fila.get("id"),
                    "tipo": fila.get("tipo_accidente"),
                    "provincia": provincia,
                    "canton": fila.get("canton"),
                    "ruta": fila.get("ruta"),
                    "descripcion": fila.get("descripcion"),
                    "fecha_hora": fila.get("fecha_hora"),
                    "latitud": coordenadas["lat"] if coordenadas else None,
                    "longitud": coordenadas["lon"] if coordenadas else None,
                    "fuente": "Nuestra base de datos"
                }
                lista_accidentes.append(Accidente)

        return lista_accidentes
    except Exception as e:
        print(f"Error al leer el archivo {archivo_ruta}: {e}")
        return []




@app.route("/") #apenas el usuario entre, esto hace que se ejecute la funcion de inicio, la cual tiene que ver con lo que ve el usuario en el html
def inicio():
    global accidentes_cache
    if not accidentes_cache: #Si la cache esta vacia, se llena con los datos del csv
        print("Cargando datos de accidentes desde el archivo CSV...")
        accidentes_cache = leer_Accidentes_csv() #Esto es lo que hace que se llene la cache con los datos del csv, y asi no tener que leer el csv cada vez que el usuario entre a la pagina, lo cual hace que la pagina sea mas rapida



    return render_template( # Esto es lo que hace que se le muestre al usuario. Toma html y le manda la lista de accidentes y averias que tenemos guardada  
        "index.html",
        accidentes=accidentes_cache
    )



@app.route("/actualizar") #Basicamente esto sirve para actualizar los datos una vez el usuario ya lleva cierto tiempo en la pagina
def actualizar():
    global accidentes_cache
    print("Actualizando datos de accidentes desde el archivo CSV...")
    accidentes_cache = leer_Accidentes_csv() #Esto es lo que hace que se actual

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

        global accidentes_cache
        if not accidentes_cache: #Si la cache esta vacia, se llena con los datos del csv
            print("Cargando datos de accidentes desde el archivo CSV...")
            accidentes_cache = leer_Accidentes_csv() #Esto es lo que hace que se llene la cache con los datos del csv, y asi no tener que leer el csv cada vez que el usuario entre a la pagina, lo cual hace que la pagina sea mas rapida


        accidentes_filtrados = [] #Esto limpia el texto para que coincida con el formato del API de  COSEVI
        for evento in accidentes_cache:

            if accidente ["provincia"].lower() in provincia_detectada.lower(): #Si la provincia del usuario, coincide con la del evento se agrega a la lista de los eventos
                accidentes_filtrados.append(evento)

        if accidentes_filtrados:   #Si hay accidentes en esta provincia los mostramos de primeros
            return render_template("index.html", eventos=accidentes_filtrados, provincia=provincia_detectada)

    except Exception as e:#En caso de error redireccionar al arranque de inicio
        print("Error detectando ubicacion", e)

    return redirect(url_for("inicio"))

if __name__ == "__main__": #Esto es lo que enciende el saervidor, que hace que solo arranque la web si se ejecuto el archivo desde la terminal
    app.run(debug=True)