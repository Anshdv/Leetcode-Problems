
def convert_num_to_bin(num):
    binary_num = ''
    use_num = num

    if use_num < 256:
        for power in range(7, -1, -1):
            remainder = use_num / (2 ** power)
            if remainder == 1.0:
                binary_num += '1'
                break
            elif remainder < 1:
                binary_num += '0'
            else:
                binary_num += '1'
                use_num -= 2 ** power
        while len(binary_num) != 8:
            binary_num += '0'

        return binary_num

    else:
        return 'number too large'


if __name__ == '__main__':
    integer = 42
    print(convert_num_to_bin(integer))  # Output: 00101010
    integer = 91
    print(convert_num_to_bin(integer))  # Output: 01011011
    integer = 255
    print(convert_num_to_bin(integer))  # Output: 11111111
