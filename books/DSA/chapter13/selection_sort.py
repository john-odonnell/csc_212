def selection_sort(array: list):
    for sorted_bubble in range(0, len(array) - 1):
        index_biggest = 0
        for j in range(1, len(array) - sorted_bubble):
            if array[j] > array[index_biggest]:
                index_biggest = j
        biggest_value = array[index_biggest]
        array[index_biggest] = array[len(array) - sorted_bubble - 1]
        array[len(array) - sorted_bubble - 1] = biggest_value


int_list = [100, 44, 0, 23, 55, 2, 77]
print(int_list)
selection_sort(int_list)
print(int_list)
