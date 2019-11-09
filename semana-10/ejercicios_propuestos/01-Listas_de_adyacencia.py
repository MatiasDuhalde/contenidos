conexiones = [(1, 2), (2, 3), (3, 2), (3, 4), (3, 5), (4, 5), (1, 6), (2, 7), (7, 10), (7, 11), (6, 8), (6, 9)]

grafo = dict()

# rellenar aquí para poblar el grafo
for origin, destiny in conexiones:
    try:
        grafo[origin].append(destiny)
    except KeyError:
        grafo[origin] = [destiny]

for nodo in grafo:
    print(f"{nodo} -> {grafo[nodo]}")
