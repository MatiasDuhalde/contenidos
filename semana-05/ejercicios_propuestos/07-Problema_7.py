import threading
import time
from threading import Thread, Lock

class Circo:
    
    vendiendo_entrada = threading.Lock()
    
    def __init__(self):
        self.entradas_vendidas = 0
        self.asientos_vendidos = [False for _ in range(1000000)]
        self.v1 = Thread(target=self.vendedor_1)
        self.v2 = Thread(target=self.vendedor_2)
        self.v3 = Thread(target=self.vendedor_3)
        
    def vender(self):
        self.v1.start()
        self.v2.start()
        self.v3.start()
        self.v1.join()
        self.v2.join()
        self.v3.join()

    def vendedor_1(self):
        for posicion in range(len(self.asientos_vendidos)):
            self.vendiendo_entrada.acquire()
            if not self.asientos_vendidos[posicion]:
                self.asientos_vendidos[posicion] = True
                self.entradas_vendidas += 1
            self.vendiendo_entrada.release()

    def vendedor_2(self):
        for posicion in range(len(self.asientos_vendidos)):
            self.vendiendo_entrada.acquire()
            if not self.asientos_vendidos[posicion]:
                self.asientos_vendidos[posicion] = True
                self.entradas_vendidas += 1
            self.vendiendo_entrada.release()

    def vendedor_3(self):
        for posicion in range(len(self.asientos_vendidos)):
            self.vendiendo_entrada.acquire()
            if not self.asientos_vendidos[posicion]:
                self.asientos_vendidos[posicion] = True
                self.entradas_vendidas += 1
            self.vendiendo_entrada.release()

                
cirque_du_soleil = Circo()
cirque_du_soleil.vender()

print(cirque_du_soleil.entradas_vendidas)