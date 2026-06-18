import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


CNFL_REFERER = (
    "https://visoresgis.cnfl.go.cr/portal/apps/webappviewer/"
    "index.html?id=a6bb9c297b1e4596b6daeea8aaf60ac4"
)
CNFL_ARCGIS_URL = (
    "https://visoresgis.cnfl.go.cr/server/rest/services/"
    "Servicio_para_las_Aver%C3%ADas_del_OMS/MapServer/0/query"
)

HEADERS = {
    "User-Agent": "radar-local-cr/1.0 (+https://www.cnfl.go.cr/)",
    "Referer": CNFL_REFERER,
}


def _zona(attributes: dict[str, Any]) -> str:
    partes = [
        attributes.get("DISTRITO"),
        attributes.get("CANTON"),
        attributes.get("PROVINCIA"),
    ]
    return "-".join(str(parte).strip() for parte in partes if parte)


def _procesar_feature(feature: dict[str, Any]) -> dict[str, Any]:
    attributes = feature.get("attributes") or {}
    geometry = feature.get("geometry") or {}

    return {
        "id": attributes.get("INCIDENCIA") or attributes.get("ESRI_OID"),
        "causa": attributes.get("CAUSADESC") or attributes.get("CAUSA"),
        "direccion": attributes.get("INCIDENTADDRESS")
        or attributes.get("DEVICEADDRESS"),
        "clientes_afectados": attributes.get("NUMCUSTOMERS"),
        "zona": _zona(attributes),
        "coordenadas": {
            "x": geometry.get("x"),
            "y": geometry.get("y"),
        },
    }


def obtener_averias_cnfl(timeout: int = 15) -> list[dict[str, Any]]:
    params = {
        "f": "json",
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "outSR": "4326",
    }

    url = f"{CNFL_ARCGIS_URL}?{urlencode(params)}"
    request = Request(url, headers=HEADERS, method="GET")

    try:
        with urlopen(request, timeout=timeout) as respuesta:
            contenido = respuesta.read().decode("utf-8")
        datos = json.loads(contenido)
    except (HTTPError, URLError, TimeoutError) as error:
        raise RuntimeError(f"Error de conexion con CNFL ArcGIS: {error}") from error
    except json.JSONDecodeError as error:
        raise RuntimeError("La respuesta de CNFL no es JSON valido") from error

    if "error" in datos:
        detalle = datos["error"].get("message", "Error desconocido de ArcGIS")
        raise RuntimeError(f"ArcGIS rechazo la consulta: {detalle}")

    features = datos.get("features")
    if not isinstance(features, list):
        raise RuntimeError("La respuesta no contiene un arreglo features")

    return [_procesar_feature(feature) for feature in features]


def main() -> None:
    try:
        averias = obtener_averias_cnfl()
    except RuntimeError as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False, indent=2))
        return

    print(json.dumps(averias, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
