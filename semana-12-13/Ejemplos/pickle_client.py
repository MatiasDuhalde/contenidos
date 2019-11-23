import pickle
import socket

server_host = socket.gethostname()  # Debemos poner aquí la dirección IP del servidor.
port = 12345


class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

# Enviaremos esta instancia de la clase Persona.
persona = Persona("Juan Pérez", "jp@ejemplo.com")
mensaje = pickle.dumps(persona)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_host, port))
sock.sendall(mensaje)

data = pickle.loads(sock.recv(4096))
print(data.nombre)
sock.close()