# Receptor mejorado del archivo.
import socket

host = socket.gethostname()
puerto = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, puerto))
sock.listen()
print('Escuchando...')

# Aceptamos un cliente.
sock_cliente, (host_cliente, puerto_cliente) = sock.accept()
print("Conexión entrante aceptada.")

# Leemos los 4 bytes del tamaño del archivo.
# Con esto transformamos una serie de bytes en un int.
largo_archivo = int.from_bytes(sock_cliente.recv(4), byteorder='big')
datos = bytearray()

# Ahora leemos el archivo por chunks, de máximo 4096 bytes.
while len(datos) < largo_archivo:
    # El último recv será probablemente más chico que 4096
    bytes_leer = min(4096, largo_archivo - len(datos))
    datos_recibidos = sock_cliente.recv(bytes_leer)
    datos.extend(datos_recibidos)

# Guardamos la información en un archivo.
with open('files/recibido.bin', 'wb') as binfile:
    binfile.write(datos)

print("¡Archivo recibido!")
# Le enviamos una respuesta a la contraparte.
sock_cliente.sendall("Gracias.".encode('utf-8'))

# Cerramos los sockets.
sock_cliente.close()
sock.close()
