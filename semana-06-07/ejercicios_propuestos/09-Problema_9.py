import sys
from PyQt5.QtCore import (pyqtSignal, QThread, QTimer)
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow)
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout)
from PyQt5.QtWidgets import (QLabel, QPushButton)
from PyQt5.QtGui import (QPixmap, QColor)
from time import sleep


class MorphThread(QThread):

    senal_morph = pyqtSignal(float, float)

    def __init__(self, cuadrado, achicandose, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cuadrado = cuadrado
        self.achicandose = achicandose

    def run(self):
        if self.cuadrado.width() == 25:
            self.achicandose = False
        if self.cuadrado.width() == 75:
            self.achicandose = True
        if self.achicandose:
            self.cuadrado.resize(self.cuadrado.width() - 1, self.cuadrado.height() - 1)
            print(self.cuadrado.width(), self.cuadrado.height())
        else:
            self.cuadrado.resize(self.cuadrado.width() + 1, self.cuadrado.height() + 1)
            print(self.cuadrado.width(), self.cuadrado.height())




class CoreWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        
        # Main Layout
        main_vbox = QVBoxLayout()
        
        # Squares
        hbox = QHBoxLayout()
        
        self.cuadrado_izq = QLabel()
        self.cuadrado_izq.setBaseSize(50, 50)
        self.cuadrado_der = QLabel()
        self.cuadrado_der.setBaseSize(50, 50)
        pixmap_cuadrado = QPixmap(50, 50)
        pixmap_cuadrado.fill(QColor("green"))
        self.cuadrado_izq.setPixmap(pixmap_cuadrado)
        self.cuadrado_der.setPixmap(pixmap_cuadrado)
        hbox.addStretch(3)
        hbox.addWidget(self.cuadrado_izq)
        hbox.addStretch(1)
        hbox.addWidget(self.cuadrado_der)
        hbox.addStretch(3)
        
        main_vbox.addLayout(hbox)
        

        # Buttons
        hbox = QHBoxLayout()

        hbox.addStretch(3)
        self.boton_iniciar = QPushButton("Iniciar")
        self.boton_iniciar.clicked.connect(self.click_iniciar)
        hbox.addWidget(self.boton_iniciar)
        hbox.addStretch(1)
        self.boton_detener = QPushButton("Detener")
        self.boton_detener.clicked.connect(self.click_detener)
        hbox.addWidget(self.boton_detener)
        hbox.addStretch(3)
        
        main_vbox.addLayout(hbox)

        self.setLayout(main_vbox)

        self.thread_izq = MorphThread(self.cuadrado_izq, True)
        self.thread_der = MorphThread(self.cuadrado_der, False)
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.morph)

    def morph(self):
        self.thread_izq.start()
        self.thread_der.start()

    def click_iniciar(self):
        self.timer.start()

    def click_detener(self):
        self.timer.stop()



class Ventana(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

        self.show()


    def init_gui(self):
        self.setGeometry(300, 200, 250, 250)
        self.form = CoreWindow()
        self.setCentralWidget(self.form)



if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())
    