def counting_sort(input_string):
    output_array = [0 for _ in range(len(input_string))]  # list of 12 zeros
    count = [0 for _ in range(256)]  # list of 256 zeros

    for i in input_string:
        count[ord(i)] += 1  # fill in a number of repeatable symbols by its code in count array

    for i in range(256):
        count[i] += count[i - 1]  # calculate sum of previous and current numbers of count array

    # put current symbol of the input array to the output array to the position of symbol code in count array
    for i in range(len(input_string)):
        output_array[count[ord(input_string[i])] - 1] = input_string[i]
        count[ord(input_string[i])] -= 1

    return output_array


if __name__ == '__main__':
    test_string = "hello, world"
    print(counting_sort(test_string))
