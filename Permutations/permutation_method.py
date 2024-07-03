
def permute(array):
    array_to_use = sorted(array)
    final = []

    for num1 in array_to_use:
        for num2 in array_to_use:
            for num3 in array_to_use:
                for num4 in array_to_use:
                    if len({num1, num2, num3, num4}) == 4:
                        final.append([num1, num2, num3, num4])

    return final


if __name__ == '__main__':
    l = [3, 1, 2, 4]
    print(permute(l))
    print(len(permute(l)))
