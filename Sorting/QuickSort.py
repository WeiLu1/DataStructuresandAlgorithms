def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


def partition(arr, low, high):
    pivot_index = high
    pivot_value = arr[high]

    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    border = low

    for i in range(low, high+1):
        if arr[i] < pivot_value:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]

    return border


if __name__ == "__main__":
    unsorted = [10, 7, 8, 9, 1, 5]
    quicksort(unsorted, 0, len(unsorted) - 1)
    print(unsorted)


