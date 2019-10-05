def es_primo(nr):
    if nr > 1:
        for i in range(2, nr):
            if not (nr % i):
                return False
        return True
    return False

def iterador_primos():
    # Completar utlizando yield, recuerda que debe ser un generador
    i = 2
    while True:
        if es_primo(i):
            yield i
        i += 1
    


generador_primos = iterador_primos()
print(generador_primos)

for i in range(1, 11):
    print(f"Primo {i}: {next(generador_primos)}")