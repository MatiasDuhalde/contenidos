import sys
from PyQt5.QtCore import (pyqtSignal, QThread, QTimer, QObject, QSize, Qt)
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


class MainBackend(QObject):

    start_timer_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        # Def timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.setInterval(10)
        # Signals
        self.morph_squares_signal = None
        self.start_timer_signal.connect(self.manipulate_timer)

    def manipulate_timer(self, action):
        if action == 0:
            self.timer.stop()
        elif action == 1:
            if not self.timer.isActive():
                self.timer.start()

    def time(self):
        self.morph_squares_signal.emit()


class CoreWindow(QWidget):

    morph_squares_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Signals
        self.start_timer_signal = None
        self.morph_squares_signal.connect(self.morph_squares)
        # GUI
        self.init_gui()

    def init_gui(self):

        # Squares
        self.cuadrado_izq = QLabel(self)
        self.cuadrado_izq.setGeometry(50, 50, 50, 50)
        self.cuadrado_der = QLabel(self)
        self.cuadrado_der.setGeometry(150, 50, 50, 50)
        pixmap_cuadrado = QPixmap(75, 75)
        pixmap_cuadrado.fill(QColor("green"))
        self.cuadrado_izq.setPixmap(pixmap_cuadrado.scaled(75, 75, Qt.KeepAspectRatio))
        self.cuadrado_der.setPixmap(pixmap_cuadrado.scaled(75, 75, Qt.KeepAspectRatio))
        self.izq_exp = False
        self.der_exp = True

        self.cuadrado_izq.setMinimumSize(25, 25)
        self.cuadrado_der.setMinimumSize(25, 25)
        self.cuadrado_izq.setMaximumSize(75, 75)
        self.cuadrado_der.setMaximumSize(75, 75)

        # Buttons
        self.boton_iniciar = QPushButton("Iniciar", self)
        self.boton_iniciar.move(50, 200)
        self.boton_iniciar.resize(self.boton_iniciar.sizeHint())
        self.boton_iniciar.clicked.connect(self.click_iniciar)
        self.boton_detener = QPushButton("Detener", self)
        self.boton_detener.move(150, 200)
        self.boton_detener.resize(self.boton_detener.sizeHint())
        self.boton_detener.clicked.connect(self.click_detener)

    def morph_squares(self):
        if self.izq_exp:
            cambio = QSize(1,1)
        else:
            cambio = QSize(-1,-1)
        self.cuadrado_izq.resize(self.cuadrado_izq.size() + cambio)
        if self.cuadrado_izq.size() == QSize(75, 75):
            self.izq_exp = False
        if self.cuadrado_izq.size() == QSize(25, 25):
            self.izq_exp = True

        if self.der_exp:
            cambio = QSize(1,1)
        else:
            cambio = QSize(-1,-1)
        self.cuadrado_der.resize(self.cuadrado_der.size() + cambio)
        if self.cuadrado_der.size() == QSize(75, 75):
            self.der_exp = False
        if self.cuadrado_der.size() == QSize(25, 25):
            self.der_exp = True


    def click_iniciar(self):
        self.start_timer_signal.emit(1)

    def click_detener(self):
        self.start_timer_signal.emit(0)



class Ventana(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Declare objects
        self.main_widget = CoreWindow()
        self.main_backend = MainBackend()
        # Connect Signals
        self.connect_signals()
        # GUI
        self.init_gui()
        self.show()


    def init_gui(self):
        self.setWindowTitle("Cuadrados Cambiantes")
        self.setGeometry(300, 200, 250, 250)
        self.setFixedSize(250, 250)
        self.setCentralWidget(self.main_widget)

    def connect_signals(self):
        self.main_widget.start_timer_signal = \
            self.main_backend.start_timer_signal
        self.main_backend.morph_squares_signal = \
            self.main_widget.morph_squares_signal


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())
    