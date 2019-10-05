from random import randint, sample

class Misterio:
    def __init__(self, atributo_1, atributo_2, atributo_3):
        self.atributo_1 = atributo_1
        self.atributo_2 = atributo_2
        self._atributo_3 = atributo_3   # ATENCIÓN AQUÍ
    
    # ¿Todo bien con estas properties?
    @property
    def atributo_3(self):
        return self._atributo_3
    
    @atributo_3.setter
    def atributo_3(self, value):
        if value % 2:  # ¿A qué se compara esto?
            self._atributo_3 = value + 1   # ERROR
        else:
            self._atributo_3 = value   # ERROR
        # Atributo_3 será siempre impar
    
    def __add__(self, otro):
        return self.atributo_1 + otro.atributo_1
    
    def __str__(self):
        return f'Atributo 1 : {self.atributo_1} - Atributo 2 : {self.atributo_2} - Atributo_3 : {self._atributo_3}'
    
    def __repr__(self):
        return f'Atributo 1 : {self.atributo_1} - Atributo 2 : {self.atributo_2} - Atributo_3 : {self._atributo_3}'

class CajaMisteriosa:
    abcedario = list('abcdefghijklmnopqrstuvwxyz')  # ¿Esto se puede?
    def __init__(self):
        # ¿Qué clase de Python es este?
        self.caja = [Misterio(randint(1, 100), ''.join(sample(CajaMisteriosa.abcedario,i)), i) for i in range(10)]
    
    def __add__(self, misterio):
        # ¿Y este add tendrá algo malo?
        haremos_algo_de_seguro = False
        for algo in filter(lambda x: x.atributo_1 == misterio.atributo_1, self.caja):
            # ¿Todo bien con la conversion de tipos?
            algo.atributo_3 = len(misterio.atributo_2) * misterio.atributo_3
            haremos_algo_de_seguro = True
        if not haremos_algo_de_seguro:  # Nuevamente no comparamos, ¿será un error?
            self.caja[-1].atributo_3 = len(misterio.atributo_2) * misterio.atributo_3

# Herencia, por supuesto, ¿Aquí debería estar el error o no?
class CajaDinamica(CajaMisteriosa):
    def __init__(self, nombre):
        self.nombre = nombre
        super().__init__()
        
    @property
    def largo(self):
        # Pero no existe self._caja ni self._largo, de seguro eso es
        return len(self.caja)
    
    @largo.setter
    def largo(self, valor):
        if type(valor) == list:
            #  Esto si que es raro no?
            self + valor[-1]
    

# Uff, ¿y si el error es en la implementacion?
if __name__ == "__main__":

    misterio_1 = Misterio(1, 'error', 3)
    mi_caja = CajaDinamica('mi caja sin error')

    # Que extraño largo al parecer funciona bien
    print(mi_caja.largo)
    mi_caja.largo += 12 
    print(mi_caja.largo)
    print(mi_caja.caja)
    mi_caja.largo = mi_caja.caja + [misterio_1]


# Resumen:
# Se cambió atributo_3 por _atributo_3 en los setter y getter de esta property.
# Como estaban definidas anteriormente, generaba error de recursión.