from Integer_to_Roman import int_to_roman, Out_of_Range
from Roman_to_Integer import roman_to_int, Invalid_Roman_Integer

try:
    operation = int(input(
        '\nEnter "1" to convert a roman numeral to a number or "2" to convert a number to a roman numeral: '
    ))

    if operation == 1:
        try:
            user_input = input('Enter a simple roman numeral to convert it to a number: ').upper()
            print(f'\n{user_input} in Roman Numerals is "{roman_to_int(user_input)}".')
        except Invalid_Roman_Integer:
            print('\nYou did not enter a valid roman numeral.')

    elif operation == 2:
        try:
            user_input = int(input('Enter a number between 1 and 3999, inclusive, to convert it to Roman Numerals: '))
            print(f'\n{user_input} in Roman Numerals is "{int_to_roman(user_input)}".')
        except Out_of_Range:
            print('\nYou did not enter a number between 1 and 3999, inclusive.')
        except ValueError:
            print('\nYou did not enter a number.')

    else:
        print('You did not enter 1 or 2.')

except ValueError:
    print('You did not enter a number.')
