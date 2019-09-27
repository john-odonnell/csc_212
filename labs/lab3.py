import time
import random
import math
import unittest

random.seed()


def int_sort(arr: list) -> list:
    """ Insertion Sort """
    arr1 = arr

    for i in range(1, len(arr1)):
        value = arr1[i]
        j = i - 1
        while j >= 0 and arr1[j] > value:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = value


def bub_sort(arr: list) -> list:
    """ Bubble Sort """
    arr1 = arr

    for i in range(0, len(arr1) - 1):
        for j in range(1, len(arr1) - i):
            if arr1[j - 1] > arr1[j]:
                arr1[j - 1], arr1[j] = arr1[j], arr1[j - 1]


def python_sort(arr: list) -> list:
    """ Python Default Sorting """
    arr1 = arr
    arr1.sort()


def gen_list_unsorted(size: int) -> list:
    """ Generates a random, unsorted list. """
    return [random.randint(-size, size) for _ in range(size)]


def gen_list_sorted(size: int) -> list:
    """ Generates a random, sorted list. """
    return sorted(gen_list_unsorted(size))


def gen_list_reversed(size: int) -> list:
    """ Generate a random, sorted list, in reversed order. """
    return sorted(gen_list_unsorted(size), reverse=True)


def gen_list_partial_sorted(size: int) -> list:
    """ Generate a random, partially sorted list. """
    A = gen_list_unsorted(size)

    if len(A) % 2 == 0:
        splice_a = A[:math.floor(size/2)]
    else:
        splice_a = A[:math.floor(size / 2)+1]
    tail = A[math.ceil(size/2):]
    return sorted(splice_a) + tail


def main():
    """ Runtime Benchmarking.
    This function should iterate through the different sorting algorithms,
    along with the various input types, and print out a table containing
    each algorithm's runtime on each input type.
    An example table is:
                Unsorted    Sorted      Reversed    Partial
    Insertion   0.000004    0.000000    0.000004    0.000004
    Bubble      0.000005    0.000005    0.000005    0.000005
    Python      0.000000    0.000000    0.000000    0.000000
    Things to be careful of:
        - Each sorting algorithm should receive the same input (generate 1 unsorted list, etc)
        - The data fields are tab separated ('\t')
        - Precision of the runtimes is rounded to 6 places
    """
    input_size = 5000  # Change this to scale your runtimes upwards or downwards.

    algo_names = ["Insertion Sort", "Bubble Sort", "Python Sort"]
    list_names = ["Random", "Sorted", "Reversed", "Partially"]

    # You can iterate over this dictionary and call the functions
    # ex: gen_func_dict['Random'](size)
    gen_func_dict = {
        "Random": gen_list_unsorted,
        "Sorted": gen_list_sorted,
        "Reversed": gen_list_reversed,
        "Partially": gen_list_partial_sorted
    }

    list_type_2print = ["Unsorted", "Sorted", "Reversed", "Partial"]
    algo_name_2print = ["Insertion", "Bubble", "Python"]

    insertion_results = []
    bubble_results = []
    python_results = []

    for name in list_names:
        input_list = gen_func_dict[name](input_size)
        for i in range(0, 3):
            if i == 0:
                start = time.time()
                int_sort(input_list)
                stop = time.time()
                insertion_results.append(stop - start)
            elif i == 1:
                start = time.time()
                bub_sort(input_list)
                stop = time.time()
                bubble_results.append(stop - start)
            elif i == 2:
                start = time.time()
                python_sort(input_list)
                stop = time.time()
                python_results.append(stop - start)

    print("\t\t", end='')
    for list_type in list_type_2print:
        if list_type == "Partial":
            print(list_type)
        elif list_type == "Sorted":
            print(list_type + "\t\t", end='')
        else:
            print(list_type + "\t", end='')

    for name in algo_name_2print:
        if name == "Insertion":
            print(name + "\t", end='')
        else:
            print(name + "\t\t", end='')

        if name == "Insertion":
            for i in range(0, 4):
                if i < 3:
                    print(str(format(insertion_results[i], '.6f')) + "\t", end='')
                else:
                    print(str(format(insertion_results[i], '.6f')))
        elif name == "Bubble":
            for i in range(0, 4):
                if i < 3:
                    print(str(format(bubble_results[i], '.6f')) + "\t", end='')
                else:
                    print(str(format(bubble_results[i], '.6f')))
        elif name == "Python":
            for i in range(0, 4):
                if i < 3:
                    print(str(format(python_results[i], '.6f')) + "\t", end='')
                else:
                    print(str(format(python_results[i], '.6f')))

    return


class Tests(unittest.TestCase):
    """ Can be used to test your sorting algorithms """

    def test_insertion(self):
        # test against sorted list
        self.assertEqual(int_sort([1,2,3,4,5,6,7,8,9,10]),[1,2,3,4,5,6,7,8,9,10])
        # test against reversed list
        self.assertEqual(int_sort([10,8,6,4,2]),[2,4,6,8,10])
        # test against list with last two elements swapped
        self.assertEqual(int_sort([3,5,7,11,9]),[3,5,7,9,11])
        # test against list with partial sorting
        self.assertEqual(int_sort([7,8,9,10,6,2,19,4]),[2,4,6,7,8,9,10,19])
        # test against list with first and last elements swapped
        self.assertEqual(int_sort([20,4,6,8,10,12,14,16,18,2]),[2,4,6,8,10,12,14,16,18,20])
        # test for list of one element
        self.assertEqual(int_sort([1]),[1])
        # test for empty list
        self.assertEqual(int_sort([]),[])
        # test with negative elements
        self.assertEqual(int_sort([2,-3,17,98,-4,-16]),[-16,-4,-3,2,17,98])
        # test with large numbers
        self.assertEqual(int_sort([738444,934855,283443]),[283443,738444,934855])
        # test with repeated elements
        self.assertEqual(int_sort([16,16,16,16,16,16,16,3,16,16,16,16,87]),[3,16,16,16,16,16,16,16,16,16,16,16,87])

    def test_bubble(self):
        # test against sorted list
        self.assertEqual(bub_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        # test against reversed list
        self.assertEqual(bub_sort([10, 8, 6, 4, 2]), [2, 4, 6, 8, 10])
        # test against list with last two elements swapped
        self.assertEqual(bub_sort([3, 5, 7, 11, 9]), [3, 5, 7, 9, 11])
        # test against list with partial sorting
        self.assertEqual(bub_sort([7, 8, 9, 10, 6, 2, 19, 4]), [2, 4, 6, 7, 8, 9, 10, 19])
        # test against list with first and last elements swapped
        self.assertEqual(bub_sort([20, 4, 6, 8, 10, 12, 14, 16, 18, 2]), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        # test for list of one element
        self.assertEqual(bub_sort([1]), [1])
        # test for empty list
        self.assertEqual(bub_sort([]), [])
        # test with negative elements
        self.assertEqual(bub_sort([2, -3, 17, 98, -4, -16]), [-16, -4, -3, 2, 17, 98])
        # test with large numbers
        self.assertEqual(bub_sort([738444, 934855, 283443]), [283443, 738444, 934855])
        # test with repeated elements
        self.assertEqual(bub_sort([16, 16, 16, 16, 16, 16, 16, 3, 16, 16, 16, 16, 87]),[3, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 87])


if __name__ == "__main__":
    # unittest.main() # Uncomment this line to run unit tests.
    main()