class ListaRecursiva:

    depth = 0

    def __init__(self):
        self.valor = None
        self.siguiente = None
        self.id_ = ListaRecursiva.depth
        ListaRecursiva.depth += 1

    def agregar(self, valor):
        '''
        Metodo que instancia cada nodo
        dependiendo de si existe alguno adyacente a él
        o no.
        '''
        nodo_nuevo = ListaRecursiva()
        nodo_nuevo.valor = valor
        nodo_actual = self.obtener(ListaRecursiva.depth - 1)
        nodo_actual.siguiente = nodo_nuevo
        print(nodo_actual.siguiente.valor)
        ListaRecursiva.depth += 1

    def __repr__(self):
        '''
        Método para representación de la lista.
        '''
        valores = []
        nodo_actual = self
        valor = str(nodo_actual.valor)
        valores.append(valor)
        while not nodo_actual.siguiente is None:
            nodo_actual = nodo_actual.siguiente
            valor = str(nodo_actual.valor)
            valores.append(valor)
        return " → " .join(valores)

    def obtener(self, posicion):
        '''
        Buscador de elemento integrante de la estructura
        '''
        nodo_actual = self
        index = 0
        while not nodo_actual.siguiente is None and index < posicion:
            nodo_actual = nodo_actual.siguiente
            index += 1
        return nodo_actual

if __name__ == '__main__':
    lista = ListaRecursiva()
    lista.agregar(1)
    print(lista)
    lista.agregar(2)
    print(lista)
    lista.agregar(3)
    print(lista)
    lista.agregar(4)
    print(lista)

    print(lista.obtener(0))
    print(lista.obtener(2))
    print(lista.obtener(3))
