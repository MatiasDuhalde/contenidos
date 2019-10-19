import sys
import os
from random import shuffle
from PyQt5.QtCore import (QObject)
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow)
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtWidgets import (QLabel, QPushButton)
from PyQt5.QtGui import (QPixmap)

class PerfilInstagram(QObject):

    def __init__(self, nombre, descripcion):
        super().__init__()
        self.nombre = QLabel("@" + nombre)
        self.descripcion = QLabel(descripcion)
        self.button_follow = QPushButton("Seguir")
        self.following = False
        self.following_switch()
        self.button_follow.clicked.connect(self.follow_button_press)
        self.button_message = QPushButton("Mensaje")
        self.foto_pixmap = QPixmap(os.path.join("..", "img", "food", "1.png"))
        self.foto = QLabel()
        self.foto.setPixmap(self.foto_pixmap)

    def follow_button_press(self):
        self.following = not self.following
        self.following_switch()

    def following_switch(self):
        if not self.following:
            self.button_follow.setStyleSheet("color: white; background-color: blue")
            self.button_follow.setText("Seguir")
        else:
            self.button_follow.setStyleSheet("color: black; background-color: white")
            self.button_follow.setText("Dejar de seguir")


class FotosInstagram(QGridLayout):

    def __init__(self, columnas, path_imagenes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnas = columnas
        self.path_imagenes = list(map(
            lambda x: os.path.join("..", "img", "food", "") + x, path_imagenes))
        self.poblar_grilla()

    def poblar_grilla(self):
        for index, path_imagen in enumerate(self.path_imagenes, start=0):
            imagen = QLabel()
            imagen.setPixmap(QPixmap(path_imagen))
            imagen.setScaledContents(True)
            self.addWidget(imagen, index // self.columnas, index % self.columnas)




class MainWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = PerfilInstagram("quicksc0per", "Hello There! I am using Whatsapp!")
        lista_imagenes = os.listdir(os.path.join("..", "img", "food"))
        shuffle(lista_imagenes)
        self.grid_fotos = FotosInstagram(4, lista_imagenes)
        self.init_gui()

    def init_gui(self):
        main_vbox = QVBoxLayout()

        main_vbox.addWidget(self.usuario.nombre)
        main_vbox.addWidget(self.usuario.descripcion)

        hbox = QHBoxLayout()
        hbox.addWidget(self.usuario.button_follow)
        hbox.addWidget(self.usuario.button_message)
        main_vbox.addLayout(hbox)

        main_vbox.addLayout(self.grid_fotos)

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
    