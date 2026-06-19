// Este archivo js sera para pedir la ubicacion al usuario en el momento en el que entra, viendo las cordanedas si es que el usuario le da permiso


if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(enviarUbicacion, errorUbicacion);
} else {
    console.log("El navegador no soporta geolocalizacion.");
}


function enviarUbicacion(posicion) {
    let lat = posicion.coords.latitude;
    let lon = posicion.coords.longitude;

    window.location.href = `/ubicacion?lat=${lat}&lon=${lon}`;

}


function errorUbicacion() {
    console.log("El usuario no quiso dar su ubicacion.");
}