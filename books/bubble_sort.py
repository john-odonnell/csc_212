def bubbleSort(array: list):
    for sorted_bubble in range(0, len(array) - 1):
        for i in range(1, len(array) - sorted_bubble):
            if array[i-1] > array[i]:
                larger_value = array[i-1]
                array[i-1] = array[i]
                array[i] = larger_value


int_list = [100, 23, 5, 77, 92, 0]
print(int_list)
bubbleSort(int_list)
print(int_list)
