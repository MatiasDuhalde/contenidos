from collections import deque

class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.conexiones = []
        
    def agregar_arista(self, nodo):
        self.conexiones.append(nodo)
    
    def __repr__(self):
        return f'{self.valor}'

    def __eq__(self, other):
        return (self.valor == other.valor) and (self.conexiones == other.conexiones)

    def __lt__(self, other):
        return self.valor < other.valor

    def __gt__(self, other):
        return self.valor > other.valor

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

    def get_nodo(self, num_nodo):
        for nodo in self.nodos:
            if nodo.valor == num_nodo:
                return nodo
        else:
            return Nodo(num_nodo)
    
    def recorrer_bfs(self, inicio=None):
        visitados = []
        if inicio is None:
            queue = deque([self.nodos[0]])
        else:
            queue = deque([self.get_nodo(inicio)])
        
        while len(queue) > 0:
            vertice = queue.popleft()
            if vertice not in visitados:
                visitados.append(vertice)
                for vecino in vertice.conexiones:
                    vecino = self.get_nodo(vecino)
                    if vecino not in visitados:
                        queue.append(vecino)
        return visitados

    def recorrer_dfs(self, inicio=None):
        visitados = []
        if inicio is None:
            stack = [self.nodos[0]]
        else:
            stack = [self.get_nodo(inicio)]
        
        while len(stack) > 0:
            vertice = stack.pop()
            if vertice not in visitados:
                visitados.append(vertice)
                for vecino in vertice.conexiones:
                    vecino = self.get_nodo(vecino)
                    if vecino not in visitados:
                        stack.append(vecino)   
        return visitados

    def encontrar_minimo(self):
        return min(self.recorrer_bfs())

    def existe_camino(self, origen, destino):
        return destino in map(lambda x: x.valor, self.recorrer_dfs(origen))

    def distancia_entre(self, origen, destino):
        visitados = []
        distancia = 0
        down = True
        queue = deque([self.get_nodo(origen)])
        
        while len(queue) > 0:
            vertice = queue.popleft()
            if vertice not in visitados:
                visitados.append(vertice)
                distancia += 1
                for vecino in vertice.conexiones:
                    vecino = self.get_nodo(vecino)
                    if vecino not in visitados:
                        queue.append(vecino)
                if destino in map(lambda x: x.valor, queue):
                    return distancia
        return float('inf')

    def existe_ciclo(self):
        visitados = []
        stack = [self.nodos[0]]
        
        while len(stack) > 0:
            vertice = stack.pop()
            if vertice in visitados:
                return True
            visitados.append(vertice)
            for vecino in vertice.conexiones:
                vecino = self.get_nodo(vecino)
                stack.append(vecino)
        return False
        

conexiones = [(1, 2), (2, 3), (3, 2), (3, 4), (3, 5), (4, 5), (1, 6), (2, 7), (7, 10), (7, 11), (6, 8), (6, 9)]

grafo = Grafo()

for conexion in conexiones:
    origen, destino = conexion
    grafo.agregar_conexion(origen, destino)

# Parte 1
print("Parte 1")
print(grafo.recorrer_bfs())

# Parte 2
print("Parte 2")
print(grafo.recorrer_dfs())

# Parte 3
print("Parte 3")
print(grafo.encontrar_minimo())

# Parte 4
print("Parte 4")
print(grafo.existe_camino(3, 5))
print(grafo.existe_camino(10, 12))

# Parte 5
print("Parte 5")
print(grafo.distancia_entre(1, 11))

# Parte 6
print("Parte 6")
print(grafo.existe_ciclo())
