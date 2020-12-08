function limpiarInputPorId(elements) {

    if (elements !== undefined) {
        for (var i = 0; i < elements.length; i += 1) {

            let input = document.getElementById(elements[i]);
            input.value = "";
        }
    }
}