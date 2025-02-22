import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMessageBox)

# Cargamos el formulario usando uic
window_name, base_class = uic.loadUiType("../qt-designer-mainwindow.ui")


class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        """Creamos las conexiones con los puertos."""
        self.pushButton1.clicked.connect(self.click_button)

    def click_button(self):
        """
        Este método controla la acción ejecuta cada vez que presionamos el
        botón1.
        """

        try:
            self.label_3.setText('= ' + str(
                float(self.lineEdit1.text()) / float(self.lineEdit2.text())))
        except ValueError as err:
            """Existen cuadros de diálogo pre-construidos. En este caso
            usaremos un MessageBox para mostrar el mensaje de error.
            """
            QMessageBox.warning(self, '', str(err))


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
