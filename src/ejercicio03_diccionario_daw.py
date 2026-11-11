def word_frequency(texto):
    frecuencia = {}

    texto = texto.lower()
    texto = texto.replace(",", "")
    texto = texto.replace(".", "")

    palabras = texto.split()

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] = frecuencia[palabra] + 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


if __name__ == "__main__":
    texto = "Programar es dificil, pero más dificil es no Programar."

    resultado = word_frequency(texto)

    print(resultado)
