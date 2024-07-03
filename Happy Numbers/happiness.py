
def is_happy(num):
    global cycle
    cycle = []
    new_num = num

    while new_num != 1:
        digit_total = 0

        for digit in str(new_num):
            digit_total += int(digit) ** 2

        if len(cycle) > 0:
            if digit_total in cycle:
                return False

        cycle.append(digit_total)
        new_num = digit_total

    else:
        return True


# a number is happy if the sum of the squares of its digits eventually leads to 1
# on each iteration, the previous sum becomes the number whose digits are squared

if __name__ == '__main__':
    print(is_happy(82))  # Output: True because 64 + 4 = 68, 36 + 64 = 100, 1 + 0 + 0 = 1
    print(is_happy(36))  # Output: False because code goes into infinite loop
