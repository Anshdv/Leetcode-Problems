from math import gcd


def all_simplified(x):
    simplified_fractions = []

    for d in range(2, x+1):
        for n in range(1, d+1):
            if int(str(n/d)[-1]) and gcd(n, d) == 1:
                simplified_fractions.append(f'{n}/{d}')

    return simplified_fractions


# the list returned consists of all the simplified fractions
# with a denominator less than or equal to "x"

if __name__ == '__main__':
    print(all_simplified(4))  # Output: ['1/2', '1/3', '2/3', '1/4', '3/4']
    print(all_simplified(6))  # Output: ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6']
