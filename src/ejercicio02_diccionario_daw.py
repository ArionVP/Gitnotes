def count_vowels(texto):

    vocales = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    texto = texto.lower()

    for letra in texto:
        if letra in vocales:
            vocales[letra] = vocales[letra] + 1

    return vocales

if __name__ == "__main__":
    
   print(count_vowels("Hola, ¿cómo estás?"))   
