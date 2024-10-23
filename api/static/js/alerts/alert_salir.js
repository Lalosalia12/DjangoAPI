document.getElementById("logout-btn").addEventListener("click", function (event) {
    event.preventDefault(); // Evita el redireccionamiento por defecto

    // SweetAlert para confirmación
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¿Deseas cerrar sesión?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, cerrar sesión',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Redirige al usuario a la URL de cierre de sesión
            window.location.href = '/salir/';
        }
    });
});