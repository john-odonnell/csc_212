def quick_sort(A: list, L: int, R: int):
    if len(A[L:R + 1]) == 0 or len(A[L:R + 1]) == 1:
        return
    else:
        P = L
        too_big = L + 1
        too_small = R

        while too_small >= too_big:
            while too_small >= too_big and A[too_big] <= A[P]:
                too_big += 1
            while A[too_small] > A[P] and too_small >= too_big:
                too_small -= 1
            if too_big < too_small:
                A[too_big], A[too_small] = A[too_small], A[too_big]
        A[P], A[too_small] = A[too_small], A[P]

        sorted = too_small

        quick_sort(A, L, sorted - 1)
        quick_sort(A, sorted + 1, R)
        return


def main():
    this_array = [5, 4, 7, 2, 8, 9, 10, 0, 1, 3, 6]
    quick_sort(this_array, 0, len(this_array) - 1)
    print(this_array)


main()
