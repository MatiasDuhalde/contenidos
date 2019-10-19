import os
import sys
from usuario import UsuarioInstagram
from interfaz import (PerfilInstagram)
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication([])
    fotos = list(map(lambda x: os.path.join("..", "img", "food", "") + x,
        os.listdir(os.path.join("..", "img", "food"))))
    usuario = UsuarioInstagram("quickscoper", "Thank god i'm a country boy!", fotos)
    ventana = PerfilInstagram(usuario)

    usuario.follow_feedback_signal = ventana.follow_feedback_signal
    ventana.follow_signal = usuario.follow_signal


    ventana.show()
    sys.exit(app.exec_())
    