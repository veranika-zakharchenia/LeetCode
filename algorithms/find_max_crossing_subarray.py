import math


def find_max_crossing_subarray(input_array):
    low = 0
    high = len(input_array)
    mid = high // 2

    left_sum = -1 * math.inf
    max_left = -1 * math.inf
    sum = 0

    i = mid
    while i > low:
        sum += input_array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
        i -= 1

    right_sum = -1 * math.inf
    sum = 0
    max_right = -1 * math.inf

    j = mid + 1
    while j < high:
        sum += input_array[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
        j += 1

    return max_left, max_right, left_sum + right_sum


if __name__ == '__main__':
    print(find_max_crossing_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
