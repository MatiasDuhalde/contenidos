from random import choice
from string import ascii_uppercase

caracter_aleatorio = lambda: choice(ascii_uppercase)

class Caracter:
    def __init__(self):
        self.valor = caracter_aleatorio()
        self.siguiente = None


class TextoAleatorio:

    def __init__(self):
        self.primer_caracter = None
        self.ultimo_caracter = None

    def agregar_nuevo_caracter(self):
        nuevo = Caracter()
        if self.primer_caracter is None:
            self.primer_caracter = nuevo
            self.ultimo_caracter = self.primer_caracter
        else:
            self.ultimo_caracter.siguiente = nuevo
            self.ultimo_caracter = self.ultimo_caracter.siguiente

    def __repr__(self):
        '''Representa la concatenación de cada caracter de la cadena de texto'''
        string_ = ""
        caracter = self.primer_caracter
        while not caracter is None:
            string_ += caracter.valor
            caracter = caracter.siguiente
        return string_

    def recorrer_texto(self):
        '''Recorrer cada caracter imprimiendo su valor y posición'''
        caracter = self.primer_caracter
        posicion = 0
        while not caracter is None:
            print(f"En posición {posicion}, el caracter es {caracter.valor}")
            caracter = caracter.siguiente
            posicion += 1

texto_1 = TextoAleatorio()
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)
texto_1.agregar_nuevo_caracter()
print(texto_1)

texto_1.recorrer_texto()
