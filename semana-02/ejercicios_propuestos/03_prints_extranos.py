class Vehiculo:
    
    def __init__(self, modelo, marca, patente):
        self.modelo = modelo
        self.marca = marca
        self.patente = patente
    
    def __str__(self):
        return f"Patente: {self.patente}\nModelo: {self.modelo}\nMarca {self.marca}"
    
    def __repr__(self):
        return f"({self.patente}, {self.modelo}, {self.marca})"

    
if __name__ == "__main__":
    auto = Vehiculo('SuperCaro', 'DCC', 'IIC2233-1')
    camion =  Vehiculo('camion', 'DCC', 'IIC2233-1')
    # Con estos prints se nota la diferencia entre repr y str
    print(auto)
    print(camion)
    print([auto, camion])