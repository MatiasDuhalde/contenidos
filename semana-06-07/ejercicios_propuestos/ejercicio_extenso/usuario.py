from PyQt5.QtCore import (pyqtSignal, QObject)

class UsuarioInstagram(QObject):

    follow_signal = pyqtSignal()

    def __init__(self, username, bio, fotos):
        super().__init__()
        self.username = username
        self.descripcion = bio
        self.fotos = fotos
        self.following = False
        self.follow_feedback_signal = None
        
        self.follow_signal.connect(self.follow)

    def follow(self):
        if self.following:
            self.follow_feedback_signal.emit(1)
        else:
            self.follow_feedback_signal.emit(0)
        self.following = not self.following
