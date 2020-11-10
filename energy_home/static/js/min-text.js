function isMinLenght(value, name, size) {

    if (value.length < size) {

        return "El campo " + name + " debe ser mayor a " + size + " caracteres.\n";
    }
    return "";
}