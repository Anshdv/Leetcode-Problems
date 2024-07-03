
def minimum_banana_rate(piles, hours):
    left, right = 1, max(piles)
    prev_rate = 0

    while True:
        my_piles, used_hrs = piles[:], 0
        rate = left + (right - left) // 2
        if prev_rate == rate:
            return right

        while sum(my_piles) != 0:
            for index, bananas in enumerate(my_piles):
                if bananas > 0:
                    my_piles[index] = bananas - rate
                    used_hrs += 1
            my_piles = [pile if pile > 0 else 0 for pile in my_piles]

        if used_hrs <= hours:
            right = prev_rate = rate
        elif used_hrs > hours:
            left = prev_rate = rate


# Koko has some piles, "p", and each number in "p" represents the number of bananas in that pile
# The guards have left her for "h" hours, and she wants to eat all the bananas in those hours
# Koko decides her bananas per hour rate as "k"
# Each hour, she chooses a pile and eats "k" bananas from that pile
# But if the pile has less than "k" bananas,
# she eats all of them in that pile and eats no more bananas for the rest of the hour
# But she wants to eat as slowly as possible
# The minimum rate of bananas per hour ("k") is returned

if __name__ == '__main__':
    p = [3, 6, 7, 11]
    h = 8
    print(minimum_banana_rate(p, h))  # Output: 4

    p = [30, 11, 23, 4, 20]
    h = 5
    print(minimum_banana_rate(p, h))  # Output: 30

    p = [30, 11, 23, 4, 20]
    h = 6
    print(minimum_banana_rate(p, h))  # Output: 23

    p = [1, 1, 1, 1, 1]
    h = 5
    print(minimum_banana_rate(p, h))  # Output: 1
