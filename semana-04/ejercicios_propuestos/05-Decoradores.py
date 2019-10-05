# crea tus decoradores aquí
from functools import wraps

def check_num_dec(n):
    def check_num(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) == n:
                return func(*args)
            else:
                print("Error, parámetros incorrectos")
        return wrapper
    return check_num
        

def check_type_dec(func):
    @wraps(func)
    def wrapper(*args):
        valid = True
        for arg in args:
            if not arg.isdigit():
                valid = False
                print("Error, parámetros incorrectos")
                break
        if valid:
            args = map(int, args)
            return func(*args)
    return wrapper

# decora aqui
@check_type_dec
@check_num_dec(2)
def suma(a, b):
    return a + b

# decora aqui
@check_type_dec
@check_num_dec(2)
def multiplicacion(a, b):
    return a * b

# decora aqui
@check_type_dec
@check_num_dec(2)
def potencia (a, b):
    return a ** b

# decora aqui
@check_type_dec
@check_num_dec(1)
def raiz(a):
    return a ** (1 / 2)

# Recordemos que al ser funciones de primera clase,
# podemos guardar las operaciones en alguna estructura de datos, 
# en particular, en un diccionario
operaciones = {1: suma,
               2: multiplicacion,
               3: potencia,
               4: raiz}


menu_inicial = '''Ingrese el número de la operación que desea realizar:
1: suma
2: multiplicacion
3: potencia
4: raiz cuadrada
>> '''

menu_numeros = '''Ingrese los números que desea operar, separados por coma
>> '''


while True:
    opcion = input(menu_inicial)
    if opcion.isdigit() and 0 < int(opcion) < 5:
        # Separamos los numeros de input
        nums = input(menu_numeros).split(',')
        # Ejecutamos la operacion correspondiente
        result = operaciones[int(opcion)](*nums)
        print(result)
    elif opcion == "exit":
        break
    else:
        print('Opción inválida')