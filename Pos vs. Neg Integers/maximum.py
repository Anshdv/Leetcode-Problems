def pos_neg_maximum(nums):
    nums.sort()

    left, right = 0, len(nums)
    while True:
        mid = (right - left) // 2
        if (nums[mid - 1] <= 0 <= nums[mid + 1]) or mid == 0:
            negatives = len([num for num in nums[:mid + 1] if num < 0])
            positives = len([num for num in nums[mid:] if num > 0])
            break
        elif mid > 0:
            right //= 2
        else:
            left //= 2

    return max(negatives, positives)


# the greater one between the number of positive numbers and number of negative numbers is returned

if __name__ == '__main__':
    array = [2, 1, -1, -1, -2, 3]
    print(pos_neg_maximum(array))  # Output: 3

    array = [-3, -2, 1, 0, 0, -1, 2]
    print(pos_neg_maximum(array))  # Output: 3

    array = [5, 20, 66, 1314, 0]
    print(pos_neg_maximum(array))  # Output: 4
