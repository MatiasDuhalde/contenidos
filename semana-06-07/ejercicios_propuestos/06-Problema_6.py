import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.QtWidgets import (QVBoxLayout)
from PyQt5.QtWidgets import (QLabel, QSpinBox)
from PyQt5.QtGui import QFont


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 200, 60)
        self.setWindowTitle('Cambia tamaño de fuente')
        
        vbox = QVBoxLayout()

        self.texto = QLabel(f"Texto", self)
        self.texto.move(10, 10)
        self.texto.resize(self.texto.sizeHint())
        self.fuente = QFont()
        vbox.addWidget(self.texto)
        
        self.caja_valor = QSpinBox(self)
        self.caja_valor.setMinimum(1)
        self.caja_valor.setMaximum(200)
        self.caja_valor.setValue(8)
        self.caja_valor.setFixedWidth(80)
        self.caja_valor.valueChanged.connect(self.change_text_size)
        vbox.addWidget(self.caja_valor)

        self.setLayout(vbox)
        self.show()

    def change_text_size(self, value):
        self.fuente.setPointSize(value)
        self.texto.setFont(self.fuente)
        self.texto.setText(f"Texto: {value}")
        self.texto.resize(self.texto.sizeHint())

        


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())