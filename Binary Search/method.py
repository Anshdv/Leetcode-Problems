
def search(array, num):
    array.sort()
    left, right = 0, len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == num:
            return array.index(num)
        elif array[middle] < num:
            left = middle + 1
        else:
            right = middle - 1

    return 'Not Found'


# using a binary search algorithm, the index of the item "num" in sorted array "array" is returned
# if "num" is not found, "Not Found" is returned

if __name__ == '__main__':
    a = [21, 52, 93, 14, 55, 86]
    n = 52
    print(f'The index of {n} in the sorted array, {a} ({sorted(a)}), is {search(a, n)}.')

