function isEmail(value, name) {

    if (!validateEmail(value)) {

        return "El campo " + name + " posee un formato incorrecto.\n";
    }
    return "";
}


function validateEmail(email) {
    let value = email
    if (/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(value)) {
        return (true)
    } else {
        return (false)
    }
}