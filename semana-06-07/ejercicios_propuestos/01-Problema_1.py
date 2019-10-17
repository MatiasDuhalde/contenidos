import sys
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint

class MiVentana(QWidget):
    def __init__(self, posicion, dimensiones, titulo):
        super().__init__()
        self.setGeometry(*posicion, *dimensiones)
        self.setWindowTitle(titulo)


if __name__ == '__main__':
    app = QApplication([])
    ventanas = []
    for i in range(0,5):
        pos = (randint(0,1500),randint(0,700))
        dim = (randint(100,500),randint(100,500))
        titulo = f"Ventana {i + 1}"
        ventanas.append(MiVentana(pos, dim, titulo))
    
    for ventana in ventanas:
        ventana.show()
    
    sys.exit(app.exec_())