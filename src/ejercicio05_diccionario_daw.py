def shopping_receipt(compra, precios):
    total_compra = 0

    for producto in compra:
        cantidad = compra[producto]
        precio = precios[producto]

        total_producto = cantidad * precio
        total_compra = total_compra + total_producto

        print(producto, cantidad, precio, round(total_producto, 2), "€")

    print("Total de la compra:", round(total_compra, 2), "€")


if __name__ == "__main__":
    compra = {
        "Apples": 2,
        "Pears": 3,
        "Oranges": 1
    }

    precios = {
        "Apples": 0.35,
        "Pears": 0.40,
        "Oranges": 0.50
    }

    shopping_receipt(compra, precios)
