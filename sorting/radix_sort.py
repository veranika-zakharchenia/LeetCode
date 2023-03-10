def counting_sort(input_array, place):
    size = len(input_array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = input_array[i] // place
        count[index % 10] += 1  # count of repeatable elements

    for i in range(1, 10):
        count[i] += count[i - 1]  # cumulative count

    i = size - 1
    while i >= 0:
        index = input_array[i] // place
        output[count[index % 10] - 1] = input_array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        input_array[i] = output[i]


def radix_sort(input_array):
    max_element = max(test_array)
    exp = 1

    while max_element // exp > 0:
        counting_sort(input_array, exp)
        exp *= 10


if __name__ == '__main__':
    test_array = [678, 98, 324, 1, 30, 897]
    radix_sort(test_array)
    print(test_array)
