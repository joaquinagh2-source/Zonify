import os
import requests
from dotenv import load_dotenv
#Este código lo que hace es conectarse al API de COSEVI para extraer los datos de accidentes en Costa Rica, los organiza en un formato limpio de filas y columnas, y devuelve una lista con los 20 reportes más recientes.
load_dotenv()


def obtener_eventos_cosevi():
    url = os.getenv("COSEVI_API_URL")
    api_key = os.getenv("COSEVI_API_KEY")

    try:
        respuesta = requests.get(
            url,
            params={"auth_key": api_key},
            timeout=10
        )

        datos = respuesta.json()

        farray = datos.get("result", {}).get("fArray", [])

        encabezados = []
        valores = []

        for item in farray:
            texto = item.get("fStr", "")

            if item.get("fHeader") is True:
                encabezados.append(texto)
            else:
                valores.append(texto)

        cantidad_columnas = len(encabezados)
        eventos = []

        for i in range(0, len(valores), cantidad_columnas):
            fila = valores[i:i + cantidad_columnas]

            if len(fila) == cantidad_columnas:
                registro = dict(zip(encabezados, fila))

                eventos.append({
                    "anio": registro.get("Año", "No disponible"),
                    "tipo": registro.get("Tipo de accidente", "No disponible"),
                    "provincia": registro.get("Provincia", "No disponible"),
                    "canton": registro.get("Cantón", "No disponible"),
                    "ruta": registro.get("Ruta", "No disponible"),
                    "sexo": registro.get("Sexo", "No disponible"),
                    "edad": registro.get("Edad", "No disponible"),
                    "fuente": "COSEVI"
                })

        return eventos[:20]

    except Exception as error:
        print("ERROR:", error)
        return []