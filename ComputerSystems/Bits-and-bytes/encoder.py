def encoder(val: int) -> bytes:
    """
    150 = 10010110
    we take 7 smalles bits
    shift right by 7
    if not 0 then add 1 to left
    otherwise break loop
    """
    out = []
    while True:
        # take 7 lowest
        byte = val & 0b1111111
        val = val >> 7
        if val != 0:
            byte = byte | 0b10000000
        out.append(byte)
        if val == 0:
            break
    return bytes(out)

def decoder(message):
    n = 0
    for byte in reversed(message):
        n = n << 7
        byte = byte & 0b01111111
        n = n | byte
    return n
    
 

if __name__ == "__main__":
    assert encoder(150) == b'\x96\x01'
    assert encoder(151) == b'\x97\x01'
    assert encoder(1) == b'\x01'
    assert decoder(b'\x96\x01') == 150
    assert decoder(b'\x97\x01') == 151
    assert decoder(b'\x01') == 1
    print('ok')
    # print(encoder(150))
    # decoded = decoder(encoded)
    # print(decoded)
    # print(decoder(b'\x96\x01'))