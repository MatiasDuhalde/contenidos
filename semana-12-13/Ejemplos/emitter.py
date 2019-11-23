# Este es el emisor del archivo.
import socket
import os

host_receptor = "DESKTOP-IRE0OII"
puerto_receptor = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nos conectamos al receptor del archivo, que ya debería estar escuchando.
sock.connect((host_receptor, puerto_receptor))
print("Conexión establecida.")

print(os.getcwd())

# Leemos el archivo y lo enviamos.
with open('files/enviar.bin', 'rb') as binfile:
    datos = binfile.read()
    sock.sendall(datos)

print("¡Archivo enviado!")

# Imprimimos lo que nos responda la contraparte.
print("Respuesta:", sock.recv(4096).decode('utf-8'))

# Cerramos el socket.
sock.close()