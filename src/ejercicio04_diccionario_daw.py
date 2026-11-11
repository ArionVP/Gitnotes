def create_dictionary(nombres, edades):
    personas = {}

    for posicion in range(len(nombres)):
        personas[nombres[posicion]] = edades[posicion]

    return personas


if __name__ == "__main__":
    nombres = ("Alice", "Bob", "Charlie")
    edades = (25, 30, 35)

    resultado = create_dictionary(nombres, edades)

    print(resultado)
