
def max_water(heights):
    max_area = counter = 0
    inside_counter = 1

    while counter < len(heights):
        while counter + inside_counter < len(heights):
            area = min(heights[counter], heights[counter + inside_counter]) * inside_counter
            if area > max_area:
                max_area = area
            inside_counter += 1

        counter += 1
        inside_counter = 1

    return max_area


# each number in "heights" is a vertical line with the height shown by the number
# 2 vertical lines form a container
# the maximum amount of water that can be held by any container formed is returned

if __name__ == '__main__':
    maximum_water = max_water([4, 3, 2, 1, 4])  # Output: 16
    print(maximum_water)
    maximum_water = max_water([1, 8, 6, 2, 5, 4, 8, 3, 7])  # Output: 49
    print(maximum_water)
    maximum_water = max_water([1, 1])  # Output: 1
    print(maximum_water)
