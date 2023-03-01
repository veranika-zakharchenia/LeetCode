from typing import List


def insert_sort(input_array: List) -> List:
    for j in range(1, len(input_array)):
        key = input_array[j]
        i = j - 1
        while i >= 0 and input_array[i] > key:
            input_array[i + 1] = input_array[i]
            i -= 1

        input_array[i + 1] = key
    return input_array


if __name__ == "__main__":
    print(insert_sort([1, -2, -3, 2, 0]))
