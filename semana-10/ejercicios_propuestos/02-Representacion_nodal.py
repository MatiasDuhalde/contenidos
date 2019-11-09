class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.conexiones = []
        
    def agregar_arista(self, nodo):
        self.conexiones.append(nodo)
    
    def __repr__(self):
        return f'{self.valor}'

class Grafo:

    def __init__(self):
        self.nodos = []

    def crear_nodo(self, valor):
        return Nodo(valor)

    def agregar_conexion(self, valor_origen, valor_destino):
        for nodo in self.nodos:
            if nodo.valor == valor_origen:
                nodo_actual = nodo
                break
        else:
            nodo_actual = self.crear_nodo(valor_origen)
            self.nodos.append(nodo_actual)
        nodo_actual.agregar_arista(valor_destino)

    def imprimir_grafo(self):
        for nodo in self.nodos:
            print(f"{nodo.valor} -> {nodo.conexiones}")

conexiones = [(1, 2), (2, 3), (3, 2), (3, 4), (3, 5), (4, 5), (1, 6), (2, 7), (7, 10), (7, 11), (6, 8), (6, 9)]

grafo = Grafo()

for conexion in conexiones:
    origen, destino = conexion
    grafo.agregar_conexion(origen, destino)

grafo.imprimir_grafo()
