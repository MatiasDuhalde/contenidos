import sys
import os
from random import shuffle
from PyQt5.QtCore import (pyqtSignal, QThread, QTimer, QObject, QSize, Qt)
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow)
from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtWidgets import (QLabel, QPushButton)
from PyQt5.QtGui import (QPixmap, QColor)

class PerfilInstagram(QWidget):

    follow_feedback_signal = pyqtSignal(int)

    def __init__(self, usuario):
        super().__init__()
        self.label_nombre = QLabel("@" + usuario.username)
        self.label_bio = QLabel(usuario.descripcion)
        self.button_follow = QPushButton("Seguir")
        self.button_message = QPushButton("Mensaje")
        self.grid_fotos = FotosInstagram(3, usuario.fotos)
        self.init_gui()
        # Signals
        self.follow_signal = None
        self.follow_feedback_signal.connect(self.following_switch)
        self.button_follow.clicked.connect(self.follow_button_press)

    def init_gui(self):
        self.setWindowTitle("Instagram")
        self.setGeometry(300, 200, 300, 600)
        self.setFixedSize(self.width(), self.height())

        main_vbox = QVBoxLayout()

        main_vbox.addWidget(self.label_nombre)
        main_vbox.addWidget(self.label_bio)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button_follow)
        self.following_switch(1)
        hbox.addWidget(self.button_message)
        main_vbox.addLayout(hbox)

        main_vbox.addLayout(self.grid_fotos)

        self.setLayout(main_vbox)

    def follow_button_press(self):
        self.follow_signal.emit()

    def following_switch(self, switch):
        if switch == 1:
            self.button_follow.setStyleSheet("color: white; background-color: blue")
            self.button_follow.setText("Seguir")
        elif switch == 0:
            self.button_follow.setStyleSheet("color: black; background-color: white")
            self.button_follow.setText("Dejar de seguir")


class FotosInstagram(QGridLayout):

    def __init__(self, columnas, path_imagenes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnas = columnas
        self.path_imagenes = path_imagenes
        self.poblar_grilla()

    def poblar_grilla(self):
        for index, path_imagen in enumerate(self.path_imagenes, start=0):
            imagen = QLabel()
            imagen.setPixmap(QPixmap(path_imagen))
            imagen.setScaledContents(True)
            self.addWidget(imagen, index // self.columnas, index % self.columnas)
