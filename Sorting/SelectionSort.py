def selectionsort(array):

    size = len(array)

    for i in range(array):
        min_idx = i
        for j in range(i + 1, size):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
