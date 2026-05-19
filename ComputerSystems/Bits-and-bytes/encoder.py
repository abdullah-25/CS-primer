def encoder(message):
    """
    1 - get binary representation of message
    2 - add padding of 6 more bits to left
    3 - break into 2 chunks
    4 - convert to little endian
    5 - add continuation bits
    6 - return
    """
    binary = ""
    while message > 0:
        binary += (str(message % 2))
        message = message // 2
    binary = binary[::-1]

    pad_to = 7 * ((len(binary)+6) // 7)
    binary = binary.zfill(pad_to)

    chunks = [binary[i:i+7] for i in range(0, len(binary), 7)]
    chunks_rev = []
    for i in reversed(chunks):
        chunks_rev.append(i)
    for i in range(len(chunks_rev)):
        if i == len(chunks_rev)-1:
            chunks_rev[i] = "0" + chunks_rev[i]
        else:
            chunks_rev[i] = "1" + chunks_rev[i]
    chunks_rev = [int(chunk, 2) for chunk in chunks_rev]
    return bytes(chunks_rev)


def decoder(message):
    pass

if __name__ == "__main__":
    assert encoder(150) == b'\x96\x01'
    # print(encoder(150))
    # decoded = decoder(encoded)
    # print(decoded)