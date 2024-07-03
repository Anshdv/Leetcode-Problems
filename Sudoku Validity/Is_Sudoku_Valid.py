class Out_of_Range(Exception):
    pass


def is_valid_sudoku(board):
    for r in range(9):
        for s in range(9):
            board[r][s] = int(board[r][s])
            if board[r][s] < 1 or board[r][s] > 9:
                raise Out_of_Range

    numbers = [x for x in range(1, 10)]

    # check boxes
    def check_boxes(outside_start, outside_stop, inside_start, inside_stop):
        check_list = []
        for a in range(outside_start, outside_stop):
            row = board[a]
            for b in range(inside_start, inside_stop):
                check_list.append(row[b])
        for num in numbers:
            if check_list.count(num) != 1:
                return False
        return True

    for out_start in range(0, 9, 3):
        for in_start in range(0, 9, 3):
            if not check_boxes(out_start, out_start+3, in_start, in_start+3):
                return False

    for row in board:
        # check rows
        for x in numbers:
            if x not in row:
                return False

        # check columns
        for y in range(9):
            if row[y] not in numbers:
                return False

    return True


array_1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8],
]

if __name__ == '__main__':
    print(is_valid_sudoku(array_1))
