# Código funcion deformador_string
import random


def deformador_string(string):
    string_deformado = ""
    for caracter in string:
        if random.random() <= 0.5:
            string_deformado += caracter.upper()
        else:
            string_deformado += caracter.lower()
    return string_deformado

print(deformador_string("Hola, Enzo"))
