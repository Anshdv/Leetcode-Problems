
def max_increases(buildings):
    new_buildings = []
    counter = 0

    for row in buildings:
        new_row = []
        horizontal_max = max(row)

        for num in row:
            vertical_list = []
            for row2 in buildings:
                vertical_list.append(row2[counter % len(row)])
            vertical_max = max(vertical_list)
            new_row.append(min([horizontal_max, vertical_max]))
            counter += 1

        new_buildings.append(new_row)

    return new_buildings


# each number in "buildings" represents the height of that building
# the objective is to increase the height of each building as much as possible without changing the city skyline
# even when viewed from any cardinal direction
# the new heights of the buildings are returned

if __name__ == '__main__':
    grid = [[3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]]
    print(max_increases(grid))  # Output: [[8, 4, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [3, 3, 3, 3]]

    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    print(max_increases(grid))  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
