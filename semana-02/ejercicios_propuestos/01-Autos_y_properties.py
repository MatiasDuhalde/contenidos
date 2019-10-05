from datetime import date

class Vehiculo:
    
    def __init__(self, modelo, marca, patente):
        self.modelo = modelo
        self.marca = marca
        self.patente = patente
        
class Deportivo(Vehiculo):
    
    def __init__(self, modelo, marca, patente, precio, fecha_de_compra):
        Vehiculo.__init__(self, modelo, marca, patente)
        self.precio = precio
        self.fecha_de_compra = int(fecha_de_compra)
        
    def adquisicion(self):
        print(f"Auto adquirido el: {self.fecha_de_compra}")
        
    @property
    def depreciacion_acumulada(self):
        return (self.precio / 10)*(date.today().year - self.fecha_de_compra)


if __name__ == "__main__":
    auto = Deportivo('SuperCaro', 'DCC', 'IIC2233', 10000, 2017)
    auto.adquisicion()
    print(f"Modelo: {auto.modelo}\nMarca: {auto.marca}\nPatente: {auto.patente}\n\
    \rPrecio: {auto.precio}\nComprado el: {auto.fecha_de_compra}\n\
    \rDepreciacion acumulada: {auto.depreciacion_acumulada}\n ")