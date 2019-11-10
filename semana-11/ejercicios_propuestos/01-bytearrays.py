with open('malvado.mal', 'rb') as corrupted_file:
    RAW_BYTES = corrupted_file.read()
    byte_array = bytearray()
    chunks = []
    for i in range(0, len(RAW_BYTES), 8):
        chunk = bytearray(RAW_BYTES[i:i+8])
        max_ = max(chunk)
        chunk = bytearray(byte_ for byte_ in chunk if byte_ != max_)
        byte_array.extend(chunk)

with open('simpatico.bmp', 'wb') as fixed_file:
    fixed_file.write(byte_array)
