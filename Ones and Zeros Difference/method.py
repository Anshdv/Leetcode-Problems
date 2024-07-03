
def ones_minus_zeros(grid):
    row_ones = [row.count(1) for row in grid]
    row_zeros = [row.count(0) for row in grid]
    column_ones = [[row[index] for row in grid].count(1) for index in range(len(grid[0]))]
    column_zeros = [[row[index] for row in grid].count(0) for index in range(len(grid[0]))]

    differences = [[row_ones[row_index] + column_ones[column_index] - row_zeros[row_index] - column_zeros[column_index]
                    for column_index in range(len(column_ones))] for row_index in range(len(row_ones))]
    return differences


# Let the number of ones in a row be "a"
# Let the number of ones in a column be "b"
# Let the number of zeros in a row be "c"
# Let the number of zeros in a column be "d"
# an array is returned where each number is a + b - c - d

if __name__ == '__main__':
    g = [[0, 1, 1],
         [1, 0, 1],
         [0, 0, 1]]
    print(ones_minus_zeros(g))  # Output: [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]

    g = [[1, 1, 1],
         [1, 1, 1]]
    print(ones_minus_zeros(g))  # Output: [[5, 5, 5], [5, 5, 5]]
