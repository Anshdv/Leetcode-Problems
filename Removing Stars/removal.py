
def remove_stars(s):
    while '*' in s:
        i = s.index('*')
        s = s[:i-1] + s[i+1:]

    return s


# given the string "s", each star and the closest non-star letter
# to the left of it is removed from the string
# then the string is returned

if __name__ == '__main__':
    strng = 'leet**cod*e'
    print(remove_stars(strng))  # Output: "lecoe" because e, t, d and all stars are the characters removed
    strng = 'erase*****'
    print(remove_stars(strng))  # Output: "" because all letters and stars are removed
    strng = 'stap*le'
    print(remove_stars(strng))  # Output: "stale" because the letter "p" is removed
