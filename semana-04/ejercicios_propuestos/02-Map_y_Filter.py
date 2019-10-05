## INICIO EJERCICIO ANTERIOR

from collections import namedtuple

Trash = namedtuple("Trash", ["trash_1", "trash_2", "trash_3"])
with open("data/names.csv") as file:
    names = file.read().splitlines()
    
with open("data/surnames.csv") as file:
    surnames = [Trash(*data.split(",")) for data in file.read().splitlines()]

with open("data/money.csv") as file:
    money = list(map(int, file.read().splitlines()))

# 1
# Escribe tu código aquí:
# Este proceso es símil a la función filter
true_names = [name for name in names if not name.isnumeric()]

# 2
# Escribe tu código aquí:
# Este proceso es símil a la función map
true_surnames = [el.trash_3 for el in surnames]

# 3
# Escribe tu código aquí:
true_money = {cash for cash in money}

## FIN EJERCICIO ANTERIOR

datos = list(zip(true_names, true_surnames, true_money))

# 1
# Escribe tu código acá
nombres_completos = list(map(lambda x: x[0] + " " + x[1], datos))
print(nombres_completos[:5])

# 2
# Escribe tu código acá
filtrado = list(filter(lambda x: 15 >= x[2] >= 8, datos))
print(filtrado)

# 3
# Escribe tu código acá
nombres_filtro = list(map(lambda x: x[0] + " " + x[1], filtrado))
print(nombres_filtro)

# 4
# Escribe tu código acá
nombres_letra = list(map(lambda x: x[0] + " " + x[1], filter(lambda x: x[0][0] == x[1][0], datos)))
print(nombres_letra)