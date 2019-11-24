import socket
from codificar import codificar

# Este es el mensaje de ejemplo (sí, es una receta para hacer sopaipillas)
MENSAJE = ("Lo primero que hay que tener en cuenta para saber cómo hacer "
           "sopaipillas, es hacer un “volcán” con la harina dejando un hueco "
           "al medio, vierta al centro la manteca derretida con la leche o el "
           "agua, la sal y el zapallo previamente molido hasta formar una "
           "pasta suave, mezcle todo hasta formar una masa suave y elástica, "
           "esta no debe tener grumos y no se tiene que pegar a la mesa.\n"
           "\n"
           "El siguiente paso para saber cómo hacer sopaipillas es amasar la "
           "masa con un uslero o a mano dejándola de aproximadamente 5mm de "
           "grosor, luego  cortarla en  círculos de 10cm (esto es a gusto, "
           "pueden ser más gruesas y más pequeñas), se recomienda pincharlas "
           "con un tenedor para que al momento de freírlas la masa no se "
           "arruine.\n"
           "\n"
           "El último paso es freír la masa en un sartén profundo y caliente "
           "el aceite a fuego alto, para probar el aceite lance un pequeño "
           "trozo de masa, debe burbujear y flotar en la superficie, coloque "
           "de 2 a 3 sopaipillas y fríalas 1 minuto por lado, no se deben "
           "dorar demasiado. Una vez fritas se sacan de la freidora y dejan en "
           "papel absorbente.\n"
           "\n"
           "Luego de haber leído esta receta de comida típica chilena, usted "
           "ya habrá sabido cómo hacer sopaipillas.")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9002

sock.bind((host, port))
sock.listen()

socket_cliente, address = sock.accept()

try:
    BLOCKS = codificar(MENSAJE)
    # Enviar largo
    bytes_largo = BLOCKS.pop(0)
    socket_cliente.sendall(bytes_largo)
    largo = int.from_bytes(bytes_largo, byteorder="little")
    for i in range(0, largo*2//80, 2):
        socket_cliente.sendall(BLOCKS[i])
        socket_cliente.sendall(BLOCKS[i+1])
except ConnectionError as e:
    print(e)
finally:
    socket_cliente.close()
    sock.close()
