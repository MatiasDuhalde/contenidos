import threading
import time

def deletrea_palabra(palabra, periodo):
    for caracter in palabra:
        time.sleep(periodo)
        print(caracter.upper())


t1 = threading.Thread(target=deletrea_palabra, args=("flZ1",3))
t2 = threading.Thread(target=deletrea_palabra, args=("e  cIUes", 5))
t3 = threading.Thread(target=deletrea_palabra, args=("i8Hq", 7))
t1.start()
t2.start()
t3.start()