class Invalid_Matrix(Exception):
    valid = False


def rotate(matrix):
    valid = True
    length = len(matrix)

    for index in range(length):
        if length != len(matrix[index]):
            raise Invalid_Matrix

    if valid:
        matrix.reverse()

        for index in range(length):
            insert_m = [sub_m[index] for sub_m in matrix[index:]]
            matrix.insert(0, insert_m)
        del matrix[length:]

        matrix.reverse()


# "m" is a square image represented as a 2D array
# "m" is rotated 90 degrees clockwise

if __name__ == '__main__':
    try:
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate(m)
        print(m)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
        rotate(m)
        print(m)  # Output: "Invalid Matrix" because "m" was not a square
    except Invalid_Matrix:
        print('Invalid Matrix')
