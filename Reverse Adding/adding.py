
def add(l1, l2):
    l1.reverse(), l2.reverse()
    string_1 = string_2 = ''

    for n in l1:
        string_1 += str(n)
    for n in l2:
        string_2 += str(n)

    num_1, num_2 = int(string_1), int(string_2)

    answer_list = [int(num) for num in str(num_1 + num_2)]
    answer_list.reverse()

    return answer_list


# list parameters "l1" and "l2" are representing digits of a number in reverse order
# the digits of the sum of the two numbers are returned as a list in reverse order

if __name__ == '__main__':
    print(add([2, 4, 3], [5, 6, 4]))  # Output: [7, 0, 8] because 342 + 465 = 807
    print(add([0, 1], [0, 1]))  # Output: [0, 2] because 10 + 10 = 20
    print(add([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
