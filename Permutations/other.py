from math import factorial as fac


def permute(array):
    global array_to_use, final, inlist
    array_to_use = array
    final = []
    inlist = []

    def recurse(n):
        global array_to_use, final, inlist

        if n >= 1:
            for x in array_to_use:
                if x in inlist:
                    continue
                else:
                    inlist.append(x)
                    if len(set(inlist)) == 4:
                        final.append(inlist)
                        inlist = []
                    else:
                        continue
                    return recurse(n-1)
        else:
            print('inlist:', inlist)
            if len(set(inlist)) == 4:
                final.append(inlist)

    recurse(len(array_to_use))

    return f'final {final}'


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(permute(nums))
