
def triangular_sum(nums):
    new_nums = [num for num in nums]

    while len(new_nums) != 1:
        new_nums = [new_nums[index] + new_nums[index + 1]
                    if (new_nums[index] + new_nums[index + 1]) < 10
                    else (new_nums[index] + new_nums[index + 1]) % 10
                    for index in range(len(new_nums) - 1)]

    return new_nums[0]


# suppose "nums" is [1, 2, 3, 4]
# the sum of each pair of numbers in "nums" (1 & 2, 2 & 3, 3 & 4) is put into a new list: [3, 5, 7]
# the same process is repeated: [8, 12]
# any sum greater than 10 is subtracted by 10: [8, 2]
# the same process is repeated until there is only 1 number remaining: [0]
# the final number is returned

if __name__ == '__main__':
    n = [1, 2, 3, 4, 5]
    print(triangular_sum(n))  # Output: 8
    n = [5]
    print(triangular_sum(n))  # Output: 5
