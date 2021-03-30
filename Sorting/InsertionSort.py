def insertionsort(array):
    for i in range(1, len(array)):
        search_index = i
        insert_value = array[i]

        while search_index > 0 and array[search_index - 1] > insert_value:
            array[search_index] = array[search_index - 1]
            search_index -= 1

        array[search_index] = insert_value