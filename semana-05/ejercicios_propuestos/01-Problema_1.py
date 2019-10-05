import threading
import time
from random import randint

def cuenta_hasta_diez():
    nombre_thread = threading.current_thread().name
    for numero in range(1, 11):
        time.sleep(randint(1, 5))
        print(f"{nombre_thread}: {numero}...")
        
threads = [threading.Thread(name=f"Hilo n°{i}", target=cuenta_hasta_diez) for i in range(1, 6)]
for thread in threads:
    thread.start()