def bubblesort(array):
    iteration_num = len(array) - 1
    for i in range(iteration_num):
        for j in range(iteration_num):
            if array[j] > array[j+1]:
                print(array[j], array)
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


if __name__ == "__main__":
    arr = [2, 3, 6, 1, 4, 3, 7, 12, 31, 21]
    bubblesort(arr)
    print(arr)
