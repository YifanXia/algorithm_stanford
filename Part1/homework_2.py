def partition(pivot_index, unsorted_list):
    n = len(unsorted_list)
    pivot = unsorted_list[pivot_index]
    delta_num_comparison = n - 1
    # Swap the pivot element with the first one, if needed
    if pivot_index != 0:
        temp = unsorted_list[0]
        unsorted_list[0] = pivot
        unsorted_list[pivot_index] = temp

    # Keep track of two separating points
    i = 1  # the index of the last element in the "smaller-than-pivot" partition
    j = 1  # the index of the "current" element

    while j < n:
        if unsorted_list[j] > pivot:
            j += 1
        elif unsorted_list[j] <= pivot:
            temp = unsorted_list[j]
            unsorted_list[j] = unsorted_list[i]
            unsorted_list[i] = temp
            i += 1
            j += 1

    # sorted_list = unsorted_list
    # print(i, j)
    unsorted_list[0] = unsorted_list[i - 1]
    unsorted_list[i - 1] = pivot

    return unsorted_list[0:i - 1], unsorted_list[i:], delta_num_comparison, pivot


def quick_sort(original_list, get_pivot_index):
    unsorted_list = original_list
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list, 0
    else:
        pivot_index = get_pivot_index(unsorted_list)
        # pivot = unsorted_list[pivot_index]
        left_partition, right_partition, delta_comp, pivot = partition(pivot_index, unsorted_list)
        left_sorted, left_num_comparison = quick_sort(left_partition, get_pivot_index)
        right_sorted, right_num_comparison = quick_sort(right_partition, get_pivot_index)

        return left_sorted + [pivot] + right_sorted, delta_comp + left_num_comparison + right_num_comparison


def first_as_pivot():
    return 0


def last_as_pivot():
    return -1


def median_as_pivot(data):
    n = len(data)
    if n < 3:
        return 0
    else:
        k = int((len(data) - 1) / 2)
        new_list = sorted([data[0], data[k], data[-1]])
        if data[0] == new_list[1]:
            return 0
        elif data[k] == new_list[1]:
            return k
        else:
            return -1


if __name__ == "__main__":

    f = open("QuickSort.txt", "r")
    raw_data = f.readlines()
    f.close()

    data_unsorted = [int(x.strip()) for x in raw_data]
    aa, num = quick_sort(data_unsorted, median_as_pivot)

    print(num)

