function limpiarCarrito() {

    $.ajax({
        type: 'POST',
        url: '{% url "cart-clean" %}',
        data: {
            csrfmiddlewaretoken: "{{ csrf_token }}",
            action: 'clear'
        },
        success: function (response) {
            console.log('Carrito limpiado exitosamente');
        },
        error: function (xhr, errmsg, err) {
            console.log('Error al limpiar el carrito');
        }
    });
}
