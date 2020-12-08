function enviar() {

    //Obtención de la información del formulario
    let nombre = document.getElementById("nombre").value;
    let comuna = document.getElementById("comuna").value;
    let email = document.getElementById("email").value;
    let telefono = document.getElementById("telefono").value;
    let mensaje = document.getElementById("mensaje").value;
    let message = isEmpty(nombre, "NOMBRE");

    //Validación de campos del formulario
    message = message + isMaxLenght(nombre, "NOMBRE", 56);
    message = message + isMinLenght(nombre, "NOMBRE", 2);
    message = message + isEmpty(comuna, "COMUNA");
    message = message + isMaxLenght(comuna, "COMUNA", 81);
    message = message + isMinLenght(comuna, "COMUNA", 3);
    message = message + isEmpty(email, "EMAIL");
    message = message + isMaxLenght(email, "EMAIL", 71);
    message = message + isMinLenght(email, "EMAIL", 5);
    message = message + isEmail(email, "EMAIL");
    message = message + isEmpty(telefono, "TELEFONO");
    message = message + isMaxLenght(telefono, "TELEFONO", 12);
    message = message + isMinLenght(telefono, "TELEFONO", 11);
    message = message + isEmpty(mensaje, "MENSAJE");
    message = message + isMaxLenght(mensaje, "MENSAJE", 501);
    message = message + isMinLenght(mensaje, "MENSAJE", 10);

    //Mostrar Error
    if (message.length > 0) {
	
	Swal.fire({
	  icon: 'error',
	  title: 'Oops...',
	  text: 'Favor ingrese datos validos!',
	  
    })
    
    } else {
        //Mostrar mensaje de exito
				Swal.fire({
  icon: 'success',
  title: 'Exito!',
  text: 'Su mensaje ha sido enviado exitosamente'
})
		
        /*limpiarInputPorId(["nombre", "comuna", "email", "telefono", "mensaje"
        ]);*/
        document.getElementById('frm-contact').submit();
    }
}

function crearMensajeErrorYExito(type, message) {

    console.log(message);
    let divMessage = document.getElementById("message-error");
    let newMessage = "<div class=\"alert alert-" + type + " alert-dismissible fade show\" role=\"alert\">" +
        "<div id=\"message\"> " + replaceAll(message, "\n", "<br>") + " </div>" +
        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">" +
        "<span aria-hidden=\"true\">&times;</span></button></div>";
    divMessage.innerHTML = newMessage;
}