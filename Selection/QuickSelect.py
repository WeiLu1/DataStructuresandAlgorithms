def quick_select(arr, left, right, k):
    split = partition(arr, left, right)

    if split == k:
        return arr[split]
    elif split < k:
        return quick_select(arr, split+1, right, k)
    else:
        return quick_select(arr, left, split-1, k)


def parition(unsorted_arr, first_idx, last_idx):
    if first_idx == last_idx:
        return first_idx

    pivot = unsorted_arr[first_idx]
    pivot_idx = first_idx
    last_element_idx = last_idx

    less_than_pivot_idx = last_element_idx
    greater_than_pivot_idx = first_idx + 1

    while True:

        while unsorted_arr[greater_than_pivot_idx] < pivot and greater_than_pivot_idx < last_idx:
            greater_than_pivot_idx += 1
        while unsorted_arr[less_than_pivot_idx] > pivot and less_than_pivot_idx >= first_idx:
            less_than_pivot_idx -= 1

        if greater_than_pivot_idx < less_than_pivot_idx:
            temp = unsorted_arr[greater_than_pivot_idx]
            unsorted_arr[greater_than_pivot_idx] = unsorted_arr[less_than_pivot_idx]
            unsorted_arr[less_than_pivot_idx] = temp
        else:
            break

        unsorted_arr[pivot_idx] = unsorted_arr[less_than_pivot_idx]
        unsorted_arr[less_than_pivot_idx] = pivot

        return less_than_pivot_idx

