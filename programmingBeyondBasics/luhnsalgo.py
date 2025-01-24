def luhnsalgorithm(cardnumber):
    numbers = [int(x) for x in cardnumber]
    check_digit = numbers[-1]
    s = 0

    for i in range(len(numbers)-2, -1, -1): # print in reversed order leaving last digit
        current_number = numbers[i]
        if i % 2 == 0:
            s += current_number * 1
        else:
            doubling = current_number * 2
            if doubling > 9:
                s += doubling - 9
    
    check_digit_check = (10 - (s % 10)) % 10
    return check_digit_check == check_digit


if __name__ == '__main__':
    assert luhnsalgorithm('17893729974')
    assert not luhnsalgorithm('17893729975')
    print('ok')
