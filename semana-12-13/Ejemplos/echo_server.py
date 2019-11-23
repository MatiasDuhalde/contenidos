# Implementación del servidor que recibe datos y los envía de vuelta.
# Esto comúnmente se denomina como 'echo server'.
import socket

host = ''
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

sock_cliente, (host_cliente, puerto_cliente) = sock.accept()
print("Conexión desde", host_cliente, puerto_cliente)

while True:
    data = sock_cliente.recv(4096)
    if not data:
        break
    sock_cliente.sendall(data)

sock_cliente.close()
sock.close()