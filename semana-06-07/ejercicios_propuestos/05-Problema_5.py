import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtWidgets import (QPushButton, QLabel)
import os


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 200, 60)
        self.setWindowTitle('Cuenta clicks')
        
        self.cuenta_clicks = 0
        self.texto = QLabel(f"{self.cuenta_clicks} clicks", self)
        self.texto.move(10, 10)
        
        self.boton_click = QPushButton("Click!", self)
        self.boton_click.setFixedWidth(180)
        self.boton_click.move(10, 30)
        self.boton_click.clicked.connect(self.accion_click)

        self.show()
        
    def accion_click(self):
        self.cuenta_clicks += 1
        if self.cuenta_clicks == 1:
            self.texto.setText(f"{self.cuenta_clicks} click.")
        else:
            self.texto.setText(f"{self.cuenta_clicks} clicks.")
        


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())