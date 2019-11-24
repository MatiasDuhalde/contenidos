import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9002

sock.connect((host, port))

try:
    # Recibe largo mensaje
    data = sock.recv(4096)
    largo = int.from_bytes(data, byteorder="little")

    # Recibe mensaje
    message = bytearray()
    for i in range(largo):
        index = int.from_bytes(sock.recv(4), byteorder="big")
        message += bytearray(sock.recv(80))
    
    # Muestra mensaje
    print(message.decode("utf-8"))
except ConnectionError as e:
    print("Ocurrió un error.")
finally:
    sock.close()
