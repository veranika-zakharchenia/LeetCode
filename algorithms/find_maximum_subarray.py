from find_max_crossing_subarray import find_max_crossing_subarray


def find_maximum_subarray(input_array, low, high):
    if high == low:
        return low, high, input_array[low]

    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(input_array, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(input_array, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(input_array)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    print(find_maximum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 0, 15))
