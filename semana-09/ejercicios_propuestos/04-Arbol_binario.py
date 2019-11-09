# textwrap tiene varias funciones convenientes para el manejo de strings
from textwrap import indent
from collections import deque

class ArbolBinario:
    def __init__(self, id_nodo, valor=None, padre=None):
        self.id_nodo = id_nodo
        self.padre = padre
        self.valor = valor
        self.hijo_izquierdo = None
        self.hijo_derecho = None

    def obtener_nodo(self, id_nodo):
        """Obtiene el nodo con el id dado"""
        stack = deque()
        stack.append(self)

        while len(stack) > 0:
            nodo_actual = stack.pop()
            if nodo_actual.id_nodo == id_nodo:
                return nodo_actual

            if not nodo_actual.hijo_izquierdo is None:
                stack.append(nodo_actual.hijo_izquierdo)
            if not nodo_actual.hijo_derecho is None:
                stack.append(nodo_actual.hijo_derecho)
        print(f"ID {id_nodo} no encontrada.")

    def agregar_nodo(self, id_nodo, valor, id_padre, orientacion):
        """Agrega un nodo con el id y valor dado, como hijo del nodo con el id 'id_padre'"""
        nodo_padre = self.obtener_nodo(id_padre)
        nodo = ArbolBinario(id_nodo, valor, id_padre)
        if orientacion == "izquierdo":
            nodo_padre.hijo_izquierdo = nodo
        elif orientacion == "derecho":
            nodo_padre.hijo_derecho = nodo

    def __repr__(self):
        """Entrega una representación del árbol"""
        string_ = ""
        cola = deque()
        cola.append(self)

        while len(cola) > 0:
            nodo_actual = cola.popleft()
            string_ += str(nodo_actual.valor) + "\n"

            if not nodo_actual.hijo_izquierdo is None:
                cola.append(nodo_actual.hijo_izquierdo)
            if not nodo_actual.hijo_derecho is None:
                cola.append(nodo_actual.hijo_derecho)

        return string_


if __name__ == '__main__':
    raiz = ArbolBinario(0, 10)
    raiz.agregar_nodo(1, 3, 0, "izquierdo")
    raiz.agregar_nodo(2, 13, 0, "derecho")

    raiz.agregar_nodo(3, 1, 1, "izquierdo")
    raiz.agregar_nodo(4, 6, 1, "derecho")

    raiz.agregar_nodo(5, 12, 2, "izquierdo")
    raiz.agregar_nodo(6, 16, 2, "derecho")

    print(raiz)
