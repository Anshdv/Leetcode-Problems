
from convert_to_binary import convert_num_to_bin
from convert_to_integer import convert_bin_to_num

while True:
    try:
        user_input = int(input('\nEnter 1 to convert from integer to binary or 2 to convert from binary to integer: '))
        if user_input == 1:
            integer = int(input('Enter the number you want to convert to binary: '))
            answer = convert_num_to_bin(integer)
            print(f'\n{integer} in binary form is {answer}.')
            break
        elif user_input == 2:
            binary = input('Enter the binary number you want to convert to an integer: ')
            answer = convert_bin_to_num(binary)
            print(f'\n{binary} in integer form is {answer}.')
            break
        else:
            print('You did not enter "1" or "2". Try again.')
    except ValueError:
        print('You did not enter a number. Try again.')
