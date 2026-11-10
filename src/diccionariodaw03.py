precios_frutas = {
                "manzana": 2.35,
                "pera": 3.05,
                "naranja": 1.75,
                "limon": 1.95,
                "melon": 4.85,
                "sandia": 3.45,
                "platano": 2.95,
                "cereza": 5.90,
                "uva": 4.15,
                "fresa": 4.25,
                }

print(precios_frutas)

precios_frutas["fresa"] = 6.54

print(precios_frutas)

for fruta in precios_frutas:
    precios_frutas[fruta] = round(precios_frutas[fruta] * 1.10, 2) # incrementamos el precio de la fruta en un 10%

print(precios_frutas)