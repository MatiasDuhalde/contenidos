import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtWidgets import (QPushButton, QLabel, QLineEdit)
from PyQt5.QtWidgets import (QRadioButton, QSpinBox, QCheckBox)
from PyQt5.QtGui import QPixmap
import os
        


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 200, 400)
        self.setWindowTitle('Registro de usuario')
        
        # Main Layout
        main_vbox = QVBoxLayout()
        main_vbox.addStretch()

        # Logo
        hbox = QHBoxLayout()
        
        hbox.addStretch()
        ruta_logo = os.path.join('img', 'yt_logo_rgb_light.png')
        self.logo_img = QLabel(self)
        self.logo_img.setPixmap(QPixmap(ruta_logo).scaledToHeight(64))
        hbox.addWidget(self.logo_img)
        hbox.addStretch()
        
        main_vbox.addLayout(hbox)
        
        # Campos del formulario
        grilla = QGridLayout()

        # Nombre de usuario:
        grilla.addWidget(QLabel("Usuario"), 0, 0)
        campo = QLineEdit("")
        campo.setMaximumWidth(120)
        grilla.addWidget(campo, 0, 1)

        # Género
        grilla.addWidget(QLabel("Género: "), 1, 0)

        vbox = QVBoxLayout()
        vbox.addWidget(QRadioButton("Femenino"))
        vbox.addWidget(QRadioButton("Masculino"))
        vbox.addWidget(QRadioButton("No binario"))
        vbox.addWidget(QRadioButton("No mencionar"))
        grilla.addLayout(vbox, 1, 1)
        
        # Edad
        grilla.addWidget(QLabel("Edad: "), 2, 0)
        caja_edad = QSpinBox()
        caja_edad.setMaximumWidth(60)
        # El máximo por defecto es 99. Siempre debe tener un máximo.
        caja_edad.setMinimum(18)
        grilla.addWidget(caja_edad, 2, 1)

        # Configuración
        grilla.addWidget(QLabel("Configuración: "), 3, 0)
        vbox = QVBoxLayout()
        vbox.addWidget(QCheckBox("Cuenta Privada"))
        vbox.addWidget(QCheckBox("Recibir noticias"))
        vbox.addWidget(QCheckBox("Acepto términos y condiciones"))
        grilla.addLayout(vbox, 3, 1)
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(grilla)
        hbox.addStretch()

        main_vbox.addLayout(hbox)

        # Botón de continuar
        hbox = QHBoxLayout()

        hbox.addStretch()
        boton_ingreso = QPushButton("Continuar")
        boton_ingreso.setMaximumWidth(80)
        hbox.addWidget(boton_ingreso)
        hbox.addStretch()
        main_vbox.addLayout(hbox)

        main_vbox.addStretch()


        self.setLayout(main_vbox)

        self.show()
        


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())