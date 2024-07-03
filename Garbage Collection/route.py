
def collecting(houses, in_between_travel):
    global glass, metal, paper
    glass = metal = paper = 0

    def method(item):
        global glass, metal, paper
        for house in houses:
            current_index = houses.index(house)

            if item in house and item == 'G':
                glass += list(house).count(item)
            elif item in house and item == 'M':
                metal += list(house).count(item)
            elif item in house and item == 'P':
                paper += list(house).count(item)

            if house != houses[-1]:
                for house in houses[current_index + 1:]:
                    if item in house and item == 'G':
                        glass += in_between_travel[current_index]
                        break
                    elif item in house and item == 'M':
                        metal += in_between_travel[current_index]
                        break
                    elif item in house and item == 'P':
                        paper += in_between_travel[current_index]
                        break

    method('G')
    method('M')
    method('P')

    return glass + metal + paper


# each house in "houses" has 3 possible types of trash: G (glass), M (metal), or P (paper)
# each unit (1 singular letter) takes 1 minute to pick up
# each number in "in_between_travel" is the number of minutes needed to travel between
# the corresponding index of the house and the house to the right of it
# only one type of garbage truck travels at once, and it goes from left to right

if __name__ == '__main__':
    h = ["G", "P", "GP", "GG"]
    t = [2, 4, 3]
    print(collecting(h, t), 'minutes')  # Output: 21 minutes
    h = ["MMM", "PGM", "GP"]
    t = [3, 10]
    print(collecting(h, t), 'minutes')  # Output: 37 minutes

    # Explanation for 1:

    # 1st house has 1 glass (add 1)
    # truck moves from 1st house to 2nd (add 2)
    # truck moves from 2nd house to 3rd (add 4)
    # 3rd house has 1 glass (add 1)
    # truck moves from 3rd house to 4th (add 3)
    # 4th house has 2 glass (add 2)
    # glass total: 13

    # truck moves from 1st house to 2nd (add 2)
    # 2nd house has 1 paper (add 1)
    # truck moves from 2nd house to 3rd (add 4)
    # 3rd house has 1 paper (add 1)
    # paper total: 8

    # overall total: 21

    # Explanation for 2:

    # glass total: 15
    # metal total: 7
    # paper total: 15

    # overall total: 37

