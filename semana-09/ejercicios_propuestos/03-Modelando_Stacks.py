class NodoStack:

    def __init__(self, valor=None):
        self.valor = None
        self.anterior = None

class Stack:

    def __init__(self):
        self.tope = None

    def push(self, valor):
        """Agrega un elemento al tope del stack"""
        nodo = NodoStack()
        nodo.valor = valor
        nodo.anterior = self.tope
        self.tope = nodo

    def pop(self):
        """Retorna y extrae el elemento del tope del stack"""
        nodo = self.tope
        self.tope = nodo.anterior
        return nodo.valor

    def peek(self):
        """Retorna el elemento del tope del _stack_ sin extraerlo de la estructura"""
        return self.tope.valor

    def is_empty(self):
        """Retorna True si el stack está vacío"""
        return not bool(self.tope)


if __name__ == '__main__':
    mi_stack = Stack()
    mi_stack.push(1) # 1
    mi_stack.push(2) # 1, 2
    mi_stack.push(3) # 1, 2, 3
    mi_stack.push(4) # 1, 2, 3, 4
    mi_stack.push(5) # 1, 2, 3, 4, 5
    print(mi_stack.pop()) # 5
    print(mi_stack.pop()) # 4
    mi_stack.push(6) # 1, 2, 3, 6
    print(mi_stack.peek()) # 6
    mi_stack.push(7) # 1, 2, 3, 6, 7
    print(mi_stack.pop()) # 7
    print(mi_stack.pop()) # 6
    print(mi_stack.pop()) # 3
    print(mi_stack.is_empty()) # False
