def nearest_mid(input_list, lower_bound_idx, upper_bound_idx, search_value):
    return lower_bound_idx \
           + ((upper_bound_idx - lower_bound_idx) / (input_list[upper_bound_idx] - input_list[lower_bound_idx])) \
           * (search_value - input_list[lower_bound_idx])


def interpolation(ordered_list, term):
    list_size = len(ordered_list) - 1
    first_elem_idx = 0
    last_elem_idx = list_size

    while first_elem_idx <= last_elem_idx:
        mid_point = nearest_mid(ordered_list, first_elem_idx, last_elem_idx, term)

        if mid_point > last_elem_idx or mid_point < first_elem_idx:
            return None

        if ordered_list[mid_point] == term:
            return mid_point

        if term > ordered_list[mid_point]:
            first_elem_idx = mid_point + 1

        else:
            last_elem_idx = mid_point - 1

        if first_elem_idx > last_elem_idx:
            return None