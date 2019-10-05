class DCCgram:
    
    def __init__(self):
        self.usuarios = []
    
    def agregar(self, nuevo_usuario):
        if nuevo_usuario.validar() and \
        not nuevo_usuario.username in map(lambda x: x.username, self.usuarios):
            self.usuarios.append(nuevo_usuario)
        else:
            print(f"ERROR: usuario {nuevo_usuario} no pudo ser creado")
        
class Usuario:
    
    def __init__(self, username, mail, edad, rut):
        # Así validamos de inmediato los atributos
        self.__username = None
        self.__mail = None
        self.__edad = None
        self.__rut = None
        self.username = username
        self.mail = mail
        self.edad = edad
        self.rut = rut
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) <= 20:
            self.__username = value
        else:
            print("ERROR: nombre de usuario muy extenso")
    
    @property
    def mail(self):
        return self.__mail
    
    @mail.setter
    def mail(self, value):
        _, dominio = value.split("@")
        if dominio == "uc.cl":
            self.__mail = value
        else: 
            print("ERROR: correo debe tener el dominio \'uc.cl\'")
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        if value >= 18:
            self.__edad = value
        else:
            print("ERROR: debes ser mayor de edad")
        
    @property
    def rut(self):
        return self.__rut
    
    @rut.setter
    def rut(self, value):
        if len(value) <= 10 and value.count("-") == 1:
            self.__rut = value
        else:
            print("ERROR: rut invalido")
    
    def validar(self):
        return not None in [self.__username, self.__edad, self.__rut, self.__mail]
    
    def __repr__(self):
        return self.__username

if __name__ == "__main__":

    dcc_gram = DCCgram()
    u1 = Usuario('usuario1', 'usuario1@uc.cl', 17, '00000-0')
    u2 = Usuario('usuario2', 'usuario2@uc.cl', 19, '00000')
    u3 = Usuario('usuario3', 'usuario1@gmail.cl', 19, '00001-0')
    u4 = Usuario('usuario4', 'usuario4@uc.cl', 18, '00002-0')

    dcc_gram.agregar(u1)
    dcc_gram.agregar(u2)
    dcc_gram.agregar(u3)
    dcc_gram.agregar(u4)
    # Si todo ha salido bien, solo user 4 debería estar en la lista
    print(dcc_gram.usuarios)  # ¿Qué método deberias implementar para poder verlo en la lista?
                              # Se debería implementar __str__ o __repr__ en DCCgram