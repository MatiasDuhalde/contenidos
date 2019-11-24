# Código servidor de Enzo
import random
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9002

# Dejamos el socket esperando ("escuchando") por conexiones
sock.bind((host, port))
sock.listen()

# Aqui aceptamos la conexión de EnZurg
socket_cliente, address = sock.accept()


MENSAJES_SPAM = [
    "SPAM!! SPAM!! SPAM!! SPAM!! SPAM!!",
    "lalalalalalalalalalalalala",
    "Intentando sobrecargar el cliente de EnZurg",
    "La respuesta a la Vida, el Universo, y Todo lo Demás es... 42",
]

# COMPLETAR AQUI
# Cada 5 segundos debes enviar un mensaje
# de la lista MENSAJES_SPAM a EnZurg

try:
    while True:
        message = random.choice(MENSAJES_SPAM).encode("utf-8")
        socket_cliente.sendall(message)
        time.sleep(5)
except Exception as e:
    print(e)
finally:
    print("Terminando la conexión...")
    socket_cliente.close()
    sock.close()
