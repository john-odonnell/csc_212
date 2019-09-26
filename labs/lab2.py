import time
import random
import unittest

random.seed()


def num_in_list(arr: list, num: int) -> bool:
    """ Number in list

    Determine whether the given number contained in the given list.
    """
    found = False
    while not found:
        for i in arr:
            if i == num:
                found = True
    return found


def sum2_in_list(arr: list, num: int) -> bool:
    """ Sum two in list

    Determine whether or not there exists two numbers in the
    given list such that the sum of both numbers is equal to num.
    """
    found = False
    while not found:
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if (arr[i] + arr[j]) == num:
                    found = True
    return found


def sum3_in_list(arr: list, num: int) -> bool:
    """ Sum three in list

    Determine whether ot not there exists three numbers in the given
    list such that the sum of all three numbers is equal to num.
    """
    found = False
    while not found:
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if (arr[i] + arr[j] + arr[k]) == num:
                        found = True
    return found


def gen_rand_list(x: int, n: int) -> list:
    """ Generate a list of random integers
    Populates a list of length n with numbers in the range [-x, x].
    """
    return [gen_rand_int(x) for _ in range(n)]


def gen_rand_int(x: int) -> int:
    """ Random Integer
    Returns a random integer in the range [-x, x].
    """
    return random.randint(-x, x)


def main():
    """ Benchmarking

    Use this function to benchmark your functions.
    Be careful to ensure that all three methods are called
    using the same random data for each timing block.
    """
    input_values = [10, 100, 1000, 10000]
    algs = ['Alg1', 'Alg2', 'Alg3']
    list_list = []
    int_list = []

    for i in range(0, len(input_values)):
        list_list.append(gen_rand_list(input_values[i], input_values[i]))
        int_list.append(gen_rand_int(100))

    for arr in list_list:
        print(len(arr))
    for value in int_list:
        print(value)

    print("\t", end='')

    for i in range(0, len(input_values)):
        if i == 3:
            print(str(input_values[i]))
        else:
            print(str(input_values[i]) + "\t\t", end='', flush=True)

    for i in range(0, len(algs)):
        print(algs[i], end='', flush=True)

        for j in range(0, len(input_values)):
            alg_start = time.time()
            if i == 0:
                num_in_list(list_list[j], int_list[j])
            elif i == 1:
                sum2_in_list(list_list[j], int_list[j])
            else:
                sum3_in_list(list_list[j], int_list[j])
            alg_end = time.time()

            if input_values[j] == 10000:
                print("\t" + str(format((alg_end - alg_start), '.10f')))
            else:
                print("\t" + str(format((alg_end - alg_start), '.10f')), end='', flush=True)
    return


class Tests(unittest.TestCase):
    """ Lab Unit Tests
    Add your own unit tests as you see fit.
    """

    def test_num_in_list(self):
        # Basic test to make sure we can detect a number in the list
        self.assertTrue(num_in_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1))

        # Basic test to make sure we can detect the lack of a number
        self.assertFalse(num_in_list([1, 2, 3, 5, 11, 13, 17], 7))

        # Test of negative values in list and argument
        self.assertTrue(num_in_list([3, -6, 9, -12, 15, -18, 21, -24, 27, -30], -30))

        # Test of large numbers (this would upset C because of the size)
        self.assertFalse(num_in_list([-62930, 70001, 2], 70000))

        # Test for empty list
        self.assertFalse(num_in_list([], 3))

        # Test for list of one element
        self.assertTrue(num_in_list([39], 39))

        # Test for repeated elements
        self.assertTrue(num_in_list([2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2], 1))

    def test_sum2_in_list(self):
        # Basic test to test correctness
        self. assertTrue(sum2_in_list([0, 1, 2, 3, 4, 5], 5))

        # Basic test to test incorrectness
        self.assertFalse(sum2_in_list([0, 1, 2, 3, 4, 5], 10))

        # Test of negatives in list and argument
        self.assertTrue(sum2_in_list([0, -1, 2, -3, 4, -50], -50))

        # Test of large numbers
        self.assertFalse(sum2_in_list([-7000, 3, 7000], 70000))

        # Test empty
        self.assertFalse(sum2_in_list([], 5))

        # Test one element
        self.assertFalse(sum2_in_list([30], 30))

        # Test two element
        self.assertTrue(sum2_in_list([10, 20], 30))

        # Test repeated elements
        self.assertTrue(sum2_in_list([2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2], 6))

    def test_sum3_in_list(self):
        # Test correctness
        self.assertTrue(sum3_in_list([0, 1, 2, 3, 4, 5], 12))

        # Test incorrectness
        self.assertFalse(sum3_in_list([0, 1, 2, 3, 4, 5], 13))

        # Test of negatives in list and argument
        self.assertTrue(sum3_in_list([0, -1, 2, -3, 4, -5], -9))

        # Test of large numbers
        self.assertTrue(sum3_in_list([-7000, 5, 6500, 1000], 500))

        # Test empty
        self.assertFalse(sum3_in_list([], 30))

        # Test one element
        self.assertFalse(sum3_in_list([30], 30))

        # Test two elements
        self.assertFalse(sum3_in_list([20, 10], 30))

        # Test three elements
        self.assertTrue(sum3_in_list([15, 10, 5], 30))

        # Test repeated elements
        self.assertTrue(sum3_in_list([2, 2, 2, 2, 2, 3, 2, 2, 2, 4, 2, 2, 5], 12))


if __name__ == "__main__":
    # unittest.main() # Uncomment this line to run unit tests!
    main()  # Run this line to benchmark your code.
