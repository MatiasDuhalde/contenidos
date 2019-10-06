import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Ventana(QWidget):
    def __init__(self, titulo, x, y):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)

    def abrir_otra_ventana(self):
        self.hide()
        otra_ventana = Ventana("Otra ventana", 300, 100)
        otra_ventana.show()


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana("Inicial", 100, 100)
    ventana.show()
    sys.exit(app.exec_())

    # Notar que esto no funciona correctamente, ya que al terminar de ejecutar
    # la clase base, se descartan todas las variables locales de la instancia, 
    # entre ellas, la nueva ventana.