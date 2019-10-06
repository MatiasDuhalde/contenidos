import sys
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtWidgets import (QVBoxLayout)
from PyQt5.QtWidgets import (QLabel)
from PyQt5.QtGui import (QPixmap, QColor)
from math import ceil
from random import randint
from time import sleep

class MiThread(QThread):

    senal_movimiento = pyqtSignal(float, float)

    def __init__(self, cuadrado, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cuadrado = cuadrado

    def run(self):
        new_x = randint(0, 450)
        new_y = randint(0, 450)
        move_time = 500 # in ms
        interval_x = (new_x - self.cuadrado.x_pos) / move_time
        interval_y = (new_y - self.cuadrado.y_pos) / move_time
        for _ in range(1, move_time):
            sleep(1 / move_time)
            self.senal_movimiento.emit(self.cuadrado.x_pos + interval_x, 
            self.cuadrado.y_pos + interval_y)


class Cuadrado(QLabel):

    def __init__(self, x, y, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.thread_movimiento = MiThread(self)
        self.thread_movimiento.senal_movimiento.connect(self.mover)
        
        self.setFixedSize(50, 50)
        
        self.mover(x, y)
        
        pixmap_cuadrado = QPixmap(50, 50)
        pixmap_cuadrado.fill(QColor("green"))
        self.setPixmap(pixmap_cuadrado)

    def mover(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.move(self.x_pos, self.y_pos)



class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 500, 500)
        self.setWindowTitle('Sigue el cuadrado')

        x = randint(0, 450)
        y = randint(0, 450)
        self.cuadrado = Cuadrado(x, y, self)

        self.show()

    def mousePressEvent(self, event):
        if (self.cuadrado.x_pos <= event.x() <= self.cuadrado.x_pos + 50 and 
        self.cuadrado.y_pos <= event.y() <= self.cuadrado.y_pos + 50):
            self.cuadrado.thread_movimiento.start()

        


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())