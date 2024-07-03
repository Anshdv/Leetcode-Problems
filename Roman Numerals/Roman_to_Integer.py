
class Invalid_Roman_Integer(Exception):
    pass


def roman_to_int(roman_int):
    roman_int_upper = roman_int.upper()
    roman_list = list(roman_int_upper)
    length = len(roman_list)
    integer = 0
    index = 0
    prev_char = roman_list[index]
    counter = 0

    while index < length:
        char = roman_list[index]
        if char == prev_char:
            counter += 1
        else:
            counter = 0

        if counter == 4:
            raise Invalid_Roman_Integer

        if char == 'M':
            integer += 1000
        elif char == 'C':
            if index + 1 != length:
                if roman_list[index + 1] == 'M':
                    integer += 900
                    index += 1
                elif roman_list[index + 1] == 'D':
                    integer += 400
                    index += 1
                else:
                    integer += 100
            else:
                integer += 100
        elif char == 'D':
            integer += 500
        elif char == 'L':
            integer += 50
        elif char == 'X':
            if index + 1 != length:
                if roman_list[index + 1] == 'C':
                    integer += 90
                    index += 1
                elif roman_list[index + 1] == 'L':
                    integer += 40
                    index += 1
                else:
                    integer += 10
            else:
                integer += 10
        elif char == 'V':
            integer += 5
        elif char == 'I':
            if index + 1 != length:
                if roman_list[index + 1] == 'X':
                    integer += 9
                    index += 1
                elif roman_list[index + 1] == 'V':
                    integer += 4
                    index += 1
                else:
                    integer += 1
            else:
                integer += 1
        else:
            raise Invalid_Roman_Integer

        prev_char = char
        index += 1

    return integer


if __name__ == '__main__':
    strng = 'MCCLXXIV'
    print(f'{strng} as a number is "{roman_to_int(strng)}".')
    strng = 'MMMDXLIX'
    print(f'{strng} as a number is "{roman_to_int(strng)}".')
    # Output:
    # MCCLXXIV as a number is "1274".
    # MMMDXLIX as a number is "3549".
