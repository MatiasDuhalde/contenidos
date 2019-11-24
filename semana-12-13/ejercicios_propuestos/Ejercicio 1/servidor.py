# Código servidor de Enzo
import random
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9002

# Dejamos el socket esperando ("escuchando") por conexiones
sock.bind((host, port))
sock.listen()

# Aqui aceptamos la conexión de EnZurg
socket_cliente, address = sock.accept()


def deformador_string(string):
    string_deformado = ""
    for caracter in string:
        if random.random() <= 0.5:
            string_deformado += caracter.upper()
        else:
            string_deformado += caracter.lower()
    return string_deformado


# COMPLETAR AQUI
# Debes recibir el mensaje de EnZurg,
# aplicarle la función deformador_string
# y enviar ese string modificado de vuelta a EnZurg
try:
    message = socket_cliente.recv(4096).decode('utf-8')
    while message:
        new_message = deformador_string(message).encode('utf-8')
        socket_cliente.sendall(new_message)
        message = socket_cliente.recv(4096).decode('utf-8')
except UnicodeDecodeError:
    print(f"Carácter no reconocido en bytearray.")
except ConnectionError as err:
    print(err)
finally:
    socket_cliente.close()
    sock.close()
    print("Fin de la conexión.")
