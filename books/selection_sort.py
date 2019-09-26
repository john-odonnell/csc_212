def selection_sort_biggest(array: list):
    for sorted_bubble in range(0, len(array) - 1):
        index_biggest = 0
        for i in range(1, len(array) - sorted_bubble):
            if array[i] > array[index_biggest]:
                index_biggest = i
        array[len(array) - sorted_bubble - 1], array[index_biggest] = \
            array[index_biggest], array[len(array) - sorted_bubble - 1]
        # biggest_value = array[index_biggest]
        # array[index_biggest] = array[len(array) - sorted_bubble - 1]
        # array[len(array) - sorted_bubble - 1] = biggest_value


def selection_sort_smallest(array: list):
    for to_sort in range(0, len(array) - 1):
        index_smallest = to_sort
        for i in range(to_sort + 1, len(array)):
            if array[i] < array[index_smallest]:
                index_smallest = i
        array[to_sort], array[index_smallest] = array[index_smallest], array[to_sort]
        # smallest_value = array[index_smallest]
        # array[index_smallest] = array[to_sort]
        # array[to_sort] = smallest_value


def main():
    sel_sort_big = [100, 44, 0, 23, 55, 2, 77]
    print("Sel Sort Biggest")
    print(sel_sort_big)
    selection_sort_biggest(sel_sort_big)
    print(sel_sort_big)

    sel_sort_small = [112, 44, 7, 38, 111, 0, 99]
    print("Sel Sort Smallest")
    print(sel_sort_small)
    selection_sort_smallest(sel_sort_small)
    print(sel_sort_small)


# insertion, bubble and selection sort are all stable sorting algorithms
# stable sorting algorithms sort repeated elements in the same
# order that they appear in the input array
main()


# Insertion Sort
# memory: O(1)
# stable
# best case O(n)    worst case O(n^2)

# Bubble Sort
# memory: O(1)
# stable
# best case O(n^2)  worst case O(n^2)

# Selection Sort
# memory O(1)
# stable
# best case O(n^2)  worst case O(n^2)
