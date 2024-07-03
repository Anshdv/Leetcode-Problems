from calculator import calculate

e = input('\nEnter a mathematical expression where each term is separated by spaces (division will be rounded down): ')
try:
    print('\nThe answer to', e, 'is', calculate(e))
except ValueError:
    print('\nYou entered an invalid expression.')
