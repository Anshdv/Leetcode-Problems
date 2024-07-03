
def moving(boxes):
    boxes_list = list(boxes)
    operations = []
    outside_iteration_counter = 0

    for box in boxes_list:
        current_box_index = boxes_list.index(box, outside_iteration_counter)
        total = 0
        inside_iteration_counter = 0

        for iteration_box in boxes_list:
            iteration_box_index = boxes_list.index(iteration_box, inside_iteration_counter)
            if (iteration_box_index != current_box_index) and (iteration_box == '1'):
                total += abs(iteration_box_index - current_box_index)
            inside_iteration_counter += 1

        operations.append(total)
        outside_iteration_counter += 1

    return operations


# 0's are empty boxes, 1's are boxes with 1 ball
# each number in the list returned is the minimum number of
# operations needed to get all balls to that index of "b"

if __name__ == '__main__':
    b = '110'
    print(moving(b))  # Output: [1, 1, 3]
    b = '001011'
    print(moving(b))  # Output: [11, 8, 5, 4, 3, 4]
