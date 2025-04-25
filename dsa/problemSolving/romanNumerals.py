def int_to_roman(n):
    parts = [
        {1000:'M'},
        {900:'CM'},
        {500:'D'},
        {400:'CD'},
        {100:'C'},
        {90:'XC'},
        {50:'L'},
        {40: 'XL'},
        {10:'X'},
        {9:'IX'},
        {5: 'V'},
        {4:'IV'},
        {1:'I'},

    ]

    for i in parts:
        # i.keys() returns object view so need to convert to list then get first value
        value = list(i.keys())[0] 
        symbol = i[value]
        if value <= n:
            return  symbol + int_to_roman(n - value)
    return "" 





if __name__ == '__main__':
    cases = ((28, 'XXVIII'), (2421, 'MMCDXXI'))
    for n, x in cases:
        assert int_to_roman(n) == x
    print('ok')