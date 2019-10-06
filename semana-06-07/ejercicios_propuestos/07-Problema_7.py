import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtWidgets import (QVBoxLayout)
from PyQt5.QtWidgets import (QLabel)
from PyQt5.QtGui import (QPixmap, QColor)
from random import randint

class Cuadrado(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(50, 50)
        self.mover_random()
        
        pixmap_cuadrado = QPixmap(50, 50)
        pixmap_cuadrado.fill(QColor("green"))
        self.setPixmap(pixmap_cuadrado)
        
    def mover_random(self):
        self.x_pos = randint(0, 450)
        self.y_pos = randint(0, 450)
        self.move(self.x_pos, self.y_pos)



class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 500, 500)
        self.setWindowTitle('Sigue el cuadrado')

        self.cuadrado = Cuadrado(self)

        self.show()

    def mousePressEvent(self, event):
        if (self.cuadrado.x_pos <= event.x() <= self.cuadrado.x_pos + 50 and 
        self.cuadrado.y_pos <= event.y() <= self.cuadrado.y_pos + 50):
            self.cuadrado.mover_random()

        


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())