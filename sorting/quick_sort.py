def do_partition(input_array, low, high):
    pivot = input_array[high]
    i = low - 1
    for j in range(low, high):
        if input_array[j] < pivot:
            i += 1
            input_array[i], input_array[j] = input_array[j], input_array[i]
    input_array[i + 1], input_array[high] = input_array[high], input_array[i + 1]
    return i + 1


def quick_sort(input_array, low, high):
    if low < high:
        partition_index = do_partition(input_array, low, high)
        quick_sort(input_array, low, partition_index - 1)
        quick_sort(input_array, partition_index + 1, high)


if __name__ == '__main__':
    test_array = [10, 80, 30, 90, 40, 50, 70]
    quick_sort(test_array, 0, len(test_array) - 1)
    print(test_array)
