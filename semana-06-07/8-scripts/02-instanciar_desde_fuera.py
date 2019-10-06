import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Ventana(QWidget):
    def __init__(self, titulo, x, y, otra_ventana=None):
        super().__init__()
        self.otra_ventana = otra_ventana
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)

    def abrir_otra_ventana(self):
        if self.otra_ventana:
            self.hide()
            self.otra_ventana.show()


if __name__ == '__main__':
    app = QApplication([])
    otra_ventana = Ventana("Otra ventana", 300, 100)
    ventana = Ventana("Inicial", 100, 100, otra_ventana)
    ventana.show()
    sys.exit(app.exec_())