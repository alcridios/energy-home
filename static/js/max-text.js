function isMaxLenght(value, name, size) {

    if (value.length > size) {

        return "El campo " + name + " debe ser menor a " + size + " caracteres.\n";
    }
    return "";
}