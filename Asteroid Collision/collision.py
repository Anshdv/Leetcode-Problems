
def colliding(array):

    while True:
        for asteroid in array:
            if asteroid <= 0:
                if array[array.index(asteroid) - 1] < abs(asteroid):
                    del array[array.index(asteroid) - 1]
                elif array[array.index(asteroid) - 1] > abs(asteroid):
                    del array[array.index(asteroid)]
                else:
                    del array[array.index(asteroid) - 1], array[array.index(asteroid)]

        if all(check > 0 for check in array) or all(check < 0 for check in array):
            break

    return array


# the absolute value of each number within "array" represents the size of the asteroid at that index
# if the size is positive, the asteroid moves right, otherwise left
# each asteroid moves at the same speed, so 2 asteroids moving in the same direction will never collide
# when two asteroids collide, the one with the smaller size explodes and the other stays the same

if __name__ == '__main__':
    print(colliding([10, 2, -5]))  # Output: [10]
    # because 2 collides with -5, resulting in -5 and then -5 collides with 10, resulting in 10
    print(colliding([8, -8]))  # Output: []
    print(colliding([5, 10, -5]))  # Output: [5, 10]
