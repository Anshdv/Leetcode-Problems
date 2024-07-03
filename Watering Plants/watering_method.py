
def watering_pants(plants, capacity):
    steps = 0
    use_capacity = original_capacity = capacity

    for plant in plants:
        if plant > use_capacity:
            use_capacity = original_capacity
            steps += (plants.index(plant)) * 2

        plants[plants.index(plant)] = 0
        use_capacity -= plant
        steps += 1

    return steps


# starting position is at the beginning of "p"
# each number in "p" is representing the amount of water the plant at that index needs
# "c" is the capacity of the water bucket used to water plants
# going left to right each plant is watered and if the next plant cannot be watered with
# the remaining water in the bucket, you refill teh water bucket at the beginning of "p"
# and then continue watering plants
# the number of total steps needed to water all the plants is returned

if __name__ == '__main__':
    p = [2, 2, 3, 3]
    c = 5
    print('Steps:', watering_pants(p, c))  # Output: Steps: 14
    p = [1, 1, 1, 4, 2, 3]
    c = 4
    print('Steps:', watering_pants(p, c))  # Output: Steps: 30
    p = [7, 7, 7, 7, 7, 7, 7]
    c = 8
    print('Steps:', watering_pants(p, c))  # Output: Steps: 49
