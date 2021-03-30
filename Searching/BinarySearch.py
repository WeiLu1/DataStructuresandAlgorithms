def binary_search_iterative(ordered_list, term):
    size_of_list = len(ordered_list) - 1
    idx_first_elem = 0
    idx_last_elem = size_of_list

    while idx_first_elem <= idx_last_elem:
        mid_point = (idx_first_elem + idx_last_elem) / 2

        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            idx_first_elem = mid_point + 1
        else:
            idx_last_elem = mid_point - 1

    if idx_first_elem > idx_last_elem:
        return None


def binary_search_recursive(ordered_list, idx_first_elem, idx_last_elem, term):
    if idx_last_elem < idx_first_elem:
        return None
    else:
        mid_point = idx_first_elem + ((idx_last_elem - idx_first_elem) / 2)
        if ordered_list[mid_point] > term:
            return binary_search_recursive(ordered_list, idx_first_elem, mid_point-1, term)
        elif ordered_list[mid_point] < term:
            return binary_search_recursive(ordered_list, mid_point+1, idx_last_elem, term)
        else:
            return mid_point