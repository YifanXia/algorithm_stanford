

def merge_count_split_inversions(left, right):
    split_inv = 0
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            split_inv += len(left) - i  # Number of remaining elements in the left

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, split_inv


def sort_count_inversions(array):

    n = len(array)
    if n <= 1:
        return array, 0
    else:
        half_length = int(n / 2)
        left = list(array[:half_length])
        right = list(array[half_length:])
        left_s, left_inv = sort_count_inversions(left)
        right_s, right_inv = sort_count_inversions(right)
        merged, split_inv = merge_count_split_inversions(left_s, right_s)
        return merged, left_inv + right_inv + split_inv


if __name__ == "__main__":

    f = open("IntegerArray.txt", "r")
    x = f.readlines()
    f.close()

    x = [int(n.strip()) for n in x]

    m, n = sort_count_inversions(x)

    print(n)

