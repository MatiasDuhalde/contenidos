def codificar(contenido):
    contenido_como_bytes = contenido.encode("utf-8")
    largo = len(contenido_como_bytes)
    largo_como_bytes = largo.to_bytes(4, byteorder="little")
    BLOQUES = [largo_como_bytes]
    for i in range(0, largo, 80):
        posicion_como_bytes = (i // 80).to_bytes(4, byteorder="big")
        chunk_como_bytes = contenido_como_bytes[i:80+i]
        BLOQUES.append(posicion_como_bytes)
        BLOQUES.append(chunk_como_bytes)
    return BLOQUES
