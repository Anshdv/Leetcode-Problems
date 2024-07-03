from math import trunc


def calculate(expression):
    e = str(expression).split()

    while len(e) > 1:
        if '*' in e:
            i = e.index('*')
            val = float(e[i - 1]) * float(e[i + 1])
            e[i] = str(val)
            del e[i + 1], e[i - 1]
        elif '/' in e:
            i = e.index('/')
            val = trunc(float(e[i - 1]) / float(e[i + 1]))
            e[i] = str(val)
            del e[i + 1], e[i - 1]
        elif '+' in e:
            i = e.index('+')
            val = float(e[i - 1]) + float(e[i + 1])
            e[i] = str(val)
            del e[i+1], e[i-1]
        elif '-' in e:
            i = e.index('-')
            val = float(e[i - 1]) - float(e[i + 1])
            e[i] = str(val)
            del e[i + 1], e[i - 1]

    return float(e[0])


if __name__ in '__main__':
    print(calculate('1 + 2 * 3.3'))  # Output: 7.6
    print(calculate('9 / 3 - 1.5'))  # Output: 1.5
