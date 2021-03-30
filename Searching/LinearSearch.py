def unordered_search(thelist, term):
    list_size = len(thelist)
    for i in range(list_size):
        if term == thelist[i]:
            return i
    return None


def ordered_search(thelist, term):
    list_size = len(thelist)
    for i in range(list_size):
        if term == thelist[i]:
            return i
        elif thelist[i] > term:
            return None
    return None