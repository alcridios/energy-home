function replaceAll(texts, element, newElement) {

    let words = texts.split(element);
    let newWord = "";

    for (var i = 0; i < words.length; i += 1) {

        newWord = newWord + words[i] + newElement
    }

    return newWord;
}