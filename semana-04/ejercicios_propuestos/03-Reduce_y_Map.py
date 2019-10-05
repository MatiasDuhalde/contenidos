import random
from functools import reduce

numeros = [random.randint(0, 15) for _ in range(100)]

def factorial(n):
    # Completa la función haciendo uso de reduce. 
    # Recuerda que factorial de 0 es 1. (Puedes implementar ese caso especifico sin reduce)
    if n <= 0:
        return 0
    else:
        return reduce(lambda x, y: x * y, range(1,n+1))

# Aqui haz uso de map con la función que acabas de definir:
factoriales = list(map(factorial, numeros))
print(factoriales)

def suma(n):
    # Completa la función haciendo uso de reduce.
    return reduce(lambda x, y: x + y, n)


# Aquí haz uso de la función que acabas de utilizar para calcular el promedio:
print(suma(factoriales)/len(factoriales))