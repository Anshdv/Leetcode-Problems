from Is_Sudoku_Valid import is_valid_sudoku, Out_of_Range

row_1 = list(input(
    '\nEnter the first row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_2 = list(input(
    'Enter the second row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_3 = list(input(
    'Enter the third row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_4 = list(input(
    'Enter the fourth row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_5 = list(input(
    'Enter the fifth row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_6 = list(input(
    'Enter the sixth row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_7 = list(input(
    'Enter the seventh row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_8 = list(input(
    'Enter the eighth row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))
row_9 = list(input(
    'Enter the ninth row of your sudoku (just numbers separated by nothing [extra numbers are not considered]): '
))

array = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]

try:
    if is_valid_sudoku(array):
        print('\nCongrats! Your sudoku is correct!')
    else:
        print('\nSorry, but your sudoku is wrong.')
except Out_of_Range:
    print('\nYou entered an invalid sudoku.')
except TypeError:
    print('\nYou entered a non-numeric sudoku.')

# correct sudoku
'''
798265341
235174968
614389527
482913756
167528439
359746812
546891273
923657184
871432695
'''
