import threading
import time
from random import shuffle

bebestibles = ["Vino"] * 15 + ["Pipeño"]
helados = ["Vainilla"] * 20 + ["Piña"]
shuffle(bebestibles)
shuffle(helados)

pipeño_encontrado = threading.Event()
helado_encontrado = threading.Event()

def busca_pipeño():
    print("¡Voy por el pipeño!")
    for bebestible in bebestibles:
        time.sleep(1)
        if bebestible == "Pipeño":
            print("¡Encontré el pipeño!")
            helado_encontrado.wait()
            pipeño_encontrado.set()
            print("¡Salud!")
            return
    
def busca_helado_de_piña():
    print("¡Voy por el helado de piña!")
    for helado in helados:
        time.sleep(1)
        if helado == "Piña":
            print("¡Encontré el helado!")
            pipeño_encontrado.wait()
            helado_encontrado.set()
            print("¡Salud!")
            return



thread_1 = threading.Thread(target=busca_pipeño)
thread_2 = threading.Thread(target=busca_helado_de_piña)

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print("¡Ti-ki-ti-ki-ti!")

# Output esperado

# El código no terminará de ejecutarse

# ¿Qué pasa que el código no termina de correr? ¿Puedes arreglarlo? 
# El código no termina de ejecutarse debido a que se genera un deadlock. 
# thread_1 espera a que se encuentre el helado de piña, y thread_2 espera a que 
# se encuentre el pipeño, sin señalar que ya encontraron su respectivo alimento.

# Para arreglarlo, basta con colocar el statement set antes del wait para ámbas funciones.
