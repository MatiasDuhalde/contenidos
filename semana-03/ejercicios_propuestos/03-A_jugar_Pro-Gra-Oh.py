from collections import namedtuple 
from random import randrange

class Juego:
    
    def __init__(self, turnos):
        
        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []
        
        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)
    
    def read_file(self):
        # Leer las cartas y guardarlas en una estructura de datos adecuada
        # NOTA: la primera fila del archivo son los atributos de las cartas
        with open("cards.csv") as archivo_cartas:
            archivo_cartas.readline()
            Carta = namedtuple("Carta",["nombre", "ataque", "defensa"])
            for datos_carta in archivo_cartas:
                n, atk, df = datos_carta.split(",")
                self.mazo.append(Carta(n, int(atk), int(df)))
                
    
    def repartir_cartas(self):
        # Barajar las cartas y repartirlas de a 1
        self.cartas_j1 = [self.mazo.pop(randrange(len(self.mazo))) for _ in range(5)]
        self.cartas_j2 = [self.mazo.pop(randrange(len(self.mazo))) for _ in range(5)]
    
    def atacar(self, atacante, defensa):
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        return ptos_ataque >= ptos_defensa
    
    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if i % 2:
                # Ataca el jugador 1
                # Rellenar aquí
                carta_j1 = choice(self.cartas_j1)
                carta_j2 = choice(self.cartas_j2)
                if self.atacar(carta_j1, carta_j2):
                    self.cartas_j2.remove(carta_j2)
                else:
                    self.cartas_j1.remove(carta_j1)
                
                
            else:
                # Ataca el jugador 2
                # Rellenar aquí
                carta_j1 = choice(self.cartas_j1)
                carta_j2 = choice(self.cartas_j2)
                if self.atacar(carta_j2, carta_j1):
                    self.cartas_j1.remove(carta_j1)
                else:
                    self.cartas_j2.remove(carta_j2)
            if self.cartas_j1 == []:
                print("Jugador 2 ha ganado.")
                break
            if self.cartas_j2 == []:
                print("Jugador 1 ha ganado.")
                break
        print(f"CARTAS RESTANTES:\nJ1: {self.cartas_j1}\nJ2: {self.cartas_j2}")


juego = Juego(10)