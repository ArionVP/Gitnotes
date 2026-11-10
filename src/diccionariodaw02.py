codigos = {}
codigos["Programacion"] = "MP0485"
codigos["Sistemas informaticos"] = "MP0483"
codigos["Contornos de desenvolvemento"] = "MP0487"
codigos["Bases de datos"] = "MP0484"
codigos["Linguaxes de marcas"] = "MP0373"
codigos["Formacion e orientacion laboral"] = "MP0617"

for clave in codigos: # se llama al método __iter__() del diccionario de forma implícita
    print(clave, codigos[clave])

for clave in codigos.keys():
    print(clave, codigos[clave])

for valor in codigos.values():
    print(valor)

for clave, valor in codigos.items(): # Devuelve una tupla y desempaqueta
    print(clave, valor)

for tupla in codigos.items(): # Devuelve una tupla
    print(tupla)  