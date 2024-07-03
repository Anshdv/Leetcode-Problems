
def minimum_rounds(tasks):
    nums = set(tasks)
    rounds = 0

    for num in nums:
        num_count = tasks.count(num)
        if num_count % 3 == 1 and num_count % 2 != 0:
            return -1
        elif num_count % 3 == 1 and num_count % 2 == 0:
            rounds += num_count // 2
        elif num_count % 3 == 2:
            rounds += num_count // 3 + 1
        else:
            rounds += num_count // 3

    return rounds


# each number in tasks represents that task's difficulty
# in each round, 2 or 3 tasks of the same difficulty can be completed
# the minimum number of rounds needed to complete all the tasks is returned
# if all the tasks cannot be completed, -1 is returned

if __name__ == '__main__':
    l = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    print(minimum_rounds(l))  # Output: 4
    l = [2, 3, 3]
    print(minimum_rounds(l))  # Output: -1 because there aren't 2 or 3 tasks of difficulty level 2
    l = [2, 2, 2, 2, 3, 3]
    print(minimum_rounds(l))  # Output: 3
