import struct

def conceal(val: str) -> float:
    """
    input short string (as many as 6 bytes)
    return value should behave similar to NaN
    
    NaN bit layout for float64: 
        sign (1) + exponent (11, all 1s) + mantissa (52). 
        For it to be NaN (not infinity), the mantissa must be non-zero. 
        The top mantissa bit is the "quiet/signaling" flag 
        — convention is to set it to 1 (quiet NaN).  

        That leaves 51 free bits.
    """
    # ref: https://en.wikipedia.org/wiki/Double-precision_floating-point_format
    nan = '0111111111111'
    res = 0
    final = 0

    for v in val:
        res = (res << 8) | ord(v)
    
    final = (int(nan, 2) << 64-13)

    NaN_pattern = final | res

    pack = struct.pack('>Q', NaN_pattern)
    unpack = struct.unpack('>d', pack)
    
    return unpack[0]



def extract(val: float) -> str:
    pass


    


def main():
    print(conceal('hello!'))
    print(extract(conceal('hello!')))
    
if __name__ == '__main__':
    main()

