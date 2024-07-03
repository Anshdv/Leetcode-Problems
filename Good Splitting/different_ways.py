
def good_splitting_ways(s):
    counter = 0

    for x in range(len(s)-1):
        length_1 = len(set([char for char in s[:x+1]]))
        length_2 = len(set([char for char in s[x+1:]]))

        if length_1 == length_2:
            counter += 1

    if counter > 0:
        return counter
    else:
        return -1


# a split is "good" if the amount of distinct letters
# in each of the two resulting strings is the same
# the amount of possible good splits of a given string is returned

if __name__ == '__main__':
    print(good_splitting_ways('aacaba'))  # Output: 2 because ("aac", "aba") and ("aaca", "ba")
    print(good_splitting_ways('abcd'))  # Output: 1 because ("ab", "cd")
