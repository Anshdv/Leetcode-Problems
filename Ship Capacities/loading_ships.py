
def min_ship_capacity(weights, days):
    left, right = max(weights), sum(weights)
    prev_ship_cap = fail = 0

    while True:
        ship_cap = left + (right - left) // 2
        if ship_cap == prev_ship_cap:
            if fail == 1:
                ship_cap = right
            break

        weight_sum = day_count = fail = 0

        for index, weight in enumerate(weights):
            if day_count < days:
                weight_sum += weight
                if weight_sum + weights[(index + 1) % len(weights)] > ship_cap:
                    day_count += 1
                    weight_sum = 0
            else:
                left = prev_ship_cap = ship_cap
                ship_cap = left + (right - left) // 2
                fail = 1

        if not fail:
            right = prev_ship_cap = ship_cap

    return ship_cap


# a ship has to transport items with weights given in list "w" within "d" days
# the minimum weight capacity of the ship is returned

if __name__ == '__main__':
    w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d = 5
    print(min_ship_capacity(w, d))  # Output: 15

    w = [3, 2, 2, 4, 1, 4]
    d = 3
    print(min_ship_capacity(w, d))  # Output: 6

    w = [1, 2, 3, 1, 1]
    d = 4
    print(min_ship_capacity(w, d))  # Output: 3
