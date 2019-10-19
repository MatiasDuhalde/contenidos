import sys
import os
from PyQt5.QtCore import (QObject)
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow)
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout)
from PyQt5.QtWidgets import (QLabel, QPushButton)
from PyQt5.QtGui import (QPixmap)

class PerfilInstagram(QObject):

    def __init__(self, nombre, descripcion):
        super().__init__()
        self.nombre = QLabel("@" + nombre)
        self.descripcion = QLabel(descripcion)
        self.button_follow = QPushButton("Seguir")
        self.button_message = QPushButton("Mensaje")
        self.foto_pixmap = QPixmap(os.path.join("..", "img", "food", "1.png"))
        self.foto = QLabel()
        self.foto.setPixmap(self.foto_pixmap)

class MainWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = PerfilInstagram("quicksc0per", "Hello There! I am using Whatsapp!")
        self.init_gui()

    def init_gui(self):
        main_vbox = QVBoxLayout()

        main_vbox.addWidget(self.usuario.nombre)
        main_vbox.addWidget(self.usuario.descripcion)

        hbox = QHBoxLayout()
        hbox.addWidget(self.usuario.button_follow)
        hbox.addWidget(self.usuario.button_message)
        main_vbox.addLayout(hbox)

        main_vbox.addWidget(self.usuario.foto)

        self.setLayout(main_vbox)


class Window(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_widget = MainWidget()
        self.init_gui()
        self.show()

    def init_gui(self):
        self.setWindowTitle("Instagram")
        self.setGeometry(300, 200, 300, 600)
        self.setFixedSize(self.width(), self.height())
        self.setCentralWidget(self.main_widget)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Window()
    sys.exit(app.exec_())
    