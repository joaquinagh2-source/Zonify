// Este archivo js sera para pedir la ubicacion al usuario en el momento en el que entra, viendo las cordanedas si es que el usuario le da permiso
document.addEventListener('DOMContentLoaded', function () {
    const buscador = document.getElementById('buscador-provincia');
    const tarjetas = document.querySelectorAll('.tarjeta');

    if (buscador) {
        buscador.addEventListener('input', function (e) {
            // Pasamos lo que escribe el usuario a minúsculas y le quitamos tildes básicas
            const textoBusqueda = e.target.value.toLowerCase()
                .normalize("NFD").replace(/[\u0300-\u036f]/g, "");

            tarjetas.forEach(function (tarjeta) {
                // Agarramos todo el texto que está dentro de la tarjeta
                const textoTarjeta = tarjeta.textContent.toLowerCase()
                    .normalize("NFD").replace(/[\u0300-\u036f]/g, "");

                // Si el texto de la tarjeta incluye lo que escribió el usuario, se muestra, si no se oculta
                if (textoTarjeta.includes(textoBusqueda)) {
                    tarjeta.style.display = 'flex';
                    tarjeta.style.opacity = '1';
                    tarjeta.style.transform = 'scale(1)';
                    tarjeta.style.transition = 'all 0.3s ease';
                } else {
                    tarjeta.style.display = 'none';
                }
            });
        });

        // Efecto visual: enfocar el borde del input al hacer clic
        buscador.addEventListener('focus', function () {
            buscador.style.borderColor = '#3b82f6';
            buscador.style.outline = 'none';
        });

        buscador.addEventListener('blur', function () {
            buscador.style.borderColor = '#e2e8f0';
        });
    }
});
