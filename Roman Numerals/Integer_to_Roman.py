
class Out_of_Range(Exception):
    pass


def int_to_roman(num):
    if 1 <= num <= 3999:

        list_num = list(str(num))
        list_num.reverse()
        reverse_list_num = list_num

        length = len(str(num))
        roman_list = []
        final_string = ''

        for x in range(length):

            if x == 0:
                digit = int(reverse_list_num[x])
                if 0 < digit < 4:
                    insert_string = ''
                    for y in range(digit):
                        insert_string += 'I'
                    roman_list.insert(0, insert_string)
                elif digit == 4:
                    roman_list.insert(0, 'IV')
                elif 5 <= digit <= 8:
                    insert_string = 'V'
                    for y in range(digit - 5):
                        insert_string += 'I'
                    roman_list.insert(0, insert_string)
                elif digit == 9:
                    roman_list.insert(0, 'IX')

            elif x == 1:
                digit = int(reverse_list_num[x] + '0')
                if 10 <= digit <= 30:
                    insert_string = ''
                    for y in range(int(str(digit)[0])):
                        insert_string += 'X'
                    roman_list.insert(0, insert_string)
                elif digit == 40:
                    roman_list.insert(0, 'XL')
                elif 50 <= digit <= 80:
                    insert_string = 'L'
                    for y in range(int(str(digit)[0]) - 5):
                        insert_string += 'X'
                    roman_list.insert(0, insert_string)
                elif digit == 90:
                    roman_list.insert(0, 'XC')

            elif x == 2:
                digit = int(reverse_list_num[x] + '00')
                if 100 <= digit <= 300:
                    insert_string = ''
                    for y in range(int(str(digit)[0])):
                        insert_string += 'C'
                    roman_list.insert(0, insert_string)
                elif digit == 400:
                    roman_list.insert(0, 'CD')
                elif 500 <= digit <= 800:
                    insert_string = 'D'
                    for y in range(int(str(digit)[0]) - 5):
                        insert_string += 'C'
                    roman_list.insert(0, insert_string)
                elif digit == 900:
                    roman_list.insert(0, 'CM')

            elif x == 3:
                digit = int(reverse_list_num[x] + '000')
                insert_string = ''
                for y in range(int(str(digit)[0])):
                    insert_string += 'M'
                roman_list.insert(0, insert_string)

        for a in roman_list:
            final_string += a
        return final_string

    else:
        raise Out_of_Range


if __name__ == '__main__':
    number = 1274
    print(f'{number} in Roman Numerals is "{int_to_roman(number)}".')
    number = 3549
    print(f'{number} in Roman Numerals is "{int_to_roman(number)}".')
    # Output:
    # 1274 in Roman Numerals is "MCCLXXIV".
    # 3549 in Roman Numerals is "MMMDXLIX".
