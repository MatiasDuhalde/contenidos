import threading
import time
def dormir(hora_actual, alarma):
    print(f"Tomaré una siesta, son las {hora_actual}")
    for i in range(15):
        if alarma.is_set():
            print("¡Gracias despertador, desperté a la hora!")
            return
        hora_actual += 1
        print(f"Estoy durmiendo a las {hora_actual}")
        time.sleep(1)
    print(f"¡Oh no!\nMe quedé dormido, son las {hora_actual}!!\n¡¡¡MALDITO DESPERTADOR!!!")
    
hora = 9
alarma = threading.Event()

thread = threading.Thread(target=dormir, args=[hora, alarma])
thread.start()

# ================ AGREGAR CÓDIGO DESDE AQUÍ ===================

def set_alarma():
    alarma.set()
    
timer = threading.Timer(5, set_alarma)
timer.start()