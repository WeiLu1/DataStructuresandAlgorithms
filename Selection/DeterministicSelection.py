def deterministic_select(arr, left, right, k):
    split = partition(arr, left, right)

    if split == k:
        return arr[split]
    elif split < k:
        return deterministic_select(arr, split + 1, right, k)
    else:
        return deterministic_select(arr, left, split - 1, k)


def partition(arr, first_idx, last_idx):
    if first_idx == last_idx:
        return first_idx
    else:
        nearest_median = median_of_medians(arr[first_idx:last_idx])

    nearest_median_idx = get_index_of_nearest_median(arr, first_idx, last_idx. nearest_median)

    swap(arr, first_idx, nearest_median_idx)

    pivot = arr[first_idx]
    pivot_index = first_idx
    last_element_idx = last_idx

    less_than_pivot_idx = last_element_idx
    greater_than_pivot_index = first_idx + 1


def median_of_medians(elems):
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)]
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist)/2])
    if len(medians) <= 5:
        return sorted(medians)[len(medians)/2]
    else:
        return median_of_medians(medians)


def get_index_of_nearest_median(arr, first, second, median):
    if first == second:
        return first
    else:
        return first + arr[first:second].index(median)


def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

