
def arranging(text):
    use_list = text.split()
    original_text = [word for word in use_list]

    for index in range(len(use_list)):
        use_list[index] = len(use_list[index])

    use_list.sort()

    for length in use_list:
        for word in original_text:
            if len(word) == length:
                use_list[use_list.index(length)] = word

    final_string = ''
    for word in use_list:
        final_string += word + ' '

    return final_string.capitalize()[:-1]


# the words in "text" are rearranged based on their length
# if 2 words have the same length, they are arranged in their original order

if __name__ == '__main__':
    print(arranging('Leetcode is cool'))  # Output: "Is cool leetcode"
    print(arranging('Keep calm and code on'))  # Output: "On and keep calm code"

