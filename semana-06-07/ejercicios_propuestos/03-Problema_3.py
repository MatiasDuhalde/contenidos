import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit)
from PyQt5.QtGui import QPixmap
import os

class Formulario(QGridLayout):

    def __init__(self, titulos):
        super().__init__()
        for i in range(len(titulos)):

            label = QLabel(f"{titulos[i]}: ")
            campo = QLineEdit("")
            campo.setFixedWidth(160)

            self.addWidget(label, i, 0)
            self.addWidget(campo, i, 1)
        


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 200, 400)
        self.setWindowTitle('Iniciar Sesión')
        
        # Main Layout
        vbox = QVBoxLayout()
        vbox.addStretch()

        # Logo
        hbox = QHBoxLayout()
        
        hbox.addStretch()
        ruta_logo = os.path.join('img', 'yt_logo_rgb_light.png')
        self.logo_img = QLabel(self)
        self.logo_img.setPixmap(QPixmap(ruta_logo).scaledToHeight(64))
        hbox.addWidget(self.logo_img)
        hbox.addStretch()
        
        vbox.addLayout(hbox)
        

        # Formulario con campos (usuario, contraseña...)
        hbox = QHBoxLayout()
        
        hbox.addStretch()
        formulario = Formulario(["Nombre de Usuario", "Correo", "Contraseña"])
        hbox.addLayout(formulario)
        hbox.addStretch()

        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        
        hbox.addStretch()
        boton_ingreso = QPushButton("Ingresar")
        hbox.addWidget(boton_ingreso)
        hbox.addStretch()
        vbox.addLayout(hbox)

        vbox.addStretch()


        self.setLayout(vbox)

        self.show()
        


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())