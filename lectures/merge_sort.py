def merge_array(array, L, R):
    point_L = 0
    point_R = 0
    for i in range(0, len(array)):
        if point_L == len(L):
            array[i] = R[point_R]
            point_R += 1
        elif point_R == len(R):
            array[i] = L[point_L]
            point_L += 1
        elif L[point_L] <= R[point_R]:
            array[i] = L[point_L]
            point_L += 1
        else:
            array[i] = R[point_R]
            point_R += 1


def merge_sort(array):
    if len(array) == 1:
        return
    else:
        middle_index = int(len(array) / 2)
        L = array[:middle_index]
        R = array[middle_index:]

        merge_sort(L)
        merge_sort(R)

        merge_array(array, L, R)

        return


def main():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(array)
    merge_sort(array)
    print(array)


main()
