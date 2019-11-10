import json


class Pizza:
    def __init__(self, nombre, ingredientes, *args, **kwargs):
        self.nombre = nombre
        self.ingredientes = ingredientes
    def __repr__(self):
        return self.nombre
    def __str__(self):
        return 'Pizza: {} \nIngredientes:{}'.format(self.nombre, self.ingredientes)


def filtrar_comestibles(diccionario):
    # Aquí deberás cargar la lista de comestibles y quitar del atributo
    # correspondiente aquellos elementos que no lo sean
    with open('comestibles.json', 'r') as edibles_file:
        edibles = json.load(edibles_file)
        diccionario["ingredientes"] = list(filter(lambda x: x in edibles, diccionario["ingredientes"]))
    return Pizza(**diccionario)


# Carga las pizzas del archivo pizzeria.json
with open('pizzeria.json', 'r') as pizzas_file:
    pizzas = json.load(pizzas_file, object_hook=filtrar_comestibles)

# y finalmente imprime la lista de pizzas usando f-strings
for pizza in pizzas:
    print(pizza, end='\n\n')
