def game_winner(people, count):
    people_list = [person for person in range(1, people + 1)]
    index = -1
    length = len(people_list)

    while length > 1:
        for i in range(count):
            index += 1
            if index >= length:
                index = 0
        del people_list[index]
        index -= 1
        length = len(people_list)

    return people_list[0]


# The Circular Game is where "n" number of people are iterated through
# and each "c"th person is eliminated

if __name__ == '__main__':
    n = 5
    c = 2
    print('Winner:', game_winner(n, c))  # Output: "Winner: 3" because people leave in following order: 2, 4, 1, 5
    n = 6
    c = 5
    print('Winner:', game_winner(n, c))  # Output: "Winner: 1" because people leave in following order: 5, 4, 6, 2, 3
