
def days_until_warmer(temps):
    day_num = 0
    days_for_warmer = []

    for temp in temps[day_num:]:
        counter = found = 0
        for next_temp in temps[temps.index(temp, day_num) + 1:]:
            # print(temps[temps.index(temp) + 1:])
            counter += 1
            if next_temp > temp:
                days_for_warmer.append(counter)
                found = 1
                break
        if not found:
            days_for_warmer.append(0)
        day_num += 1

    return days_for_warmer


# each number in the list returned is the amount of days that the temperature
# of the corresponding index of "temperatures" (daily temperatures) needs to become warmer

if __name__ == '__main__':
    print(days_until_warmer([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    # because the first warmer temperature after 73 (0th index)
    # is the next one (74 at the 1st index) so the 0th index in the list returned is 1, etc.
    print(days_until_warmer([1, 1, 2, 1]))  # Output: [2, 1, 0, 0]
