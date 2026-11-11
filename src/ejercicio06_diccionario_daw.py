
def count_votes(elecciones):
    resultado = {}

    for opcion in elecciones:
        if opcion in resultado:
            resultado[opcion] = resultado[opcion] + 1
        else:
            resultado[opcion] = 1

    return resultado


if __name__ == "__main__":

    menu = ("Carne", "Pescado", "Verduras")
    elecciones = []

    continuar = "si"

    while continuar == "si":

        print("NEW YEAR'S EVE MENU")

        for posicion in range(len(menu)):
            print(posicion + 1, "-", menu[posicion])

        opcion = int(input("¿Que opción prefiere?: "))

        if opcion >= 1 and opcion <= len(menu):
            elecciones.append(menu[opcion - 1])
            continuar = input("¿Hay más personas? (si/no): ").lower()
        else:
            print("Opción inválida")

    resultado = count_votes(elecciones)

    print("RESULTADOS:")
    print(resultado)
