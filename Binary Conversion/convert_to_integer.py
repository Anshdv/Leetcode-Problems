
def convert_bin_to_num(bin_num):
    num = 0

    for x in range(len(str(bin_num)), 0, -1):
        if str(bin_num)[len(str(bin_num)) - x] == '1':
            num += 2 ** (x - 1)
        else:
            continue

    return num


if __name__ == '__main__':
    binary_num = '00101010'
    print(convert_bin_to_num(binary_num))  # Output: 42
    binary_num = '01011011'
    print(convert_bin_to_num(binary_num))  # Output: 91
    binary_num = '11111111'
    print(convert_bin_to_num(binary_num))  # Output: 255
