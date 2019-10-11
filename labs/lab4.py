import unittest
import time


def sum(n: int) -> int:
    """ Sum of Numbers.
    Returns the sum of all integers in the range [0, 10]
    """
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


def running_time_sum():
    values = [10, 100, 250, 500]
    run_times = []

    for value in values:
        start = time.time()
        sum(value)
        end = time.time()
        run_times.append(end - start)

    print("Run times of Sum Function:")
    for i in range(len(values)):
        print(str(values[i]) + ":\t" + str(run_times[0]))
    print("\n")


def gcd(a: int, b: int) -> int:
    """ Greatest Common Divisor.
    Returns the greatest common divisor between a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def print_nums(n: int) -> str:
    """ The Natural Numbers.
    Prints all integers in the range [1, n],
    wrapping the output every 10 numbers.
    """
    if n == 1:
        return str(n)
    else:
        if n % 10 == 0:
            return print_nums(n - 1) + " " + str(n) + "\n"
        elif n % 10 == 1:
            return print_nums(n - 1) + str(n)
        else:
            return print_nums(n - 1) + " " + str(n)


def fibonacci(n: int) -> int:
    """ Fibonacci Series.
    Returns the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def num_len(num: int) -> int:
    """ Number of Digits.
    Returns the length of an integer n.
    """
    if num < 10:
        return 1
    else:
        return 1 + num_len(int(num / 10))


class Tests(unittest.TestCase):
    """ Use these to test your algorithms """

    def test_sum(self):
        # test for simple number
        self.assertEqual(sum(10),55)
        # test for larger number
        self.assertEqual(sum(30), 465)
        # test for value 1
        self.assertEqual(sum(1),1)
        # test for value 0
        self.assertEqual(sum(0),0)
        return

    def test_gcd(self):
        # test
        self.assertEqual(gcd(10, 12), 2)
        # test
        self.assertNotEqual(gcd(10, 12), 6)
        # test
        self.assertEqual(gcd(81, 96), 3)
        # test
        self.assertEqual(gcd(1, 1), 1)
        # test
        self.assertEqual(gcd(11, 0), 11)
        # test
        self.assertEqual(gcd(0, 0), 0)

    def test_print_nums(self):
        self.assertEqual(print_nums(35), "1 2 3 4 5 6 7 8 9 10\n11 12 13 14 15 16 17 18 19 20\n"
                                         "21 22 23 24 25 26 27 28 29 30\n"
                                         "31 32 33 34 35")

    def test_fibonacci(self):
        # test
        self.assertEqual(fibonacci(2), 1)
        # test
        self.assertEqual(fibonacci(4), 3)
        # test
        self.assertEqual(fibonacci(10), 55)

    def test_num_len(self):
        # test
        self.assertEqual(num_len(1), 1)
        # test
        self.assertEqual(num_len(11), 2)
        # test
        self.assertEqual(num_len(12345), 5)
        # test
        self.assertEqual(num_len(0), 1)
        # test
        self.assertNotEqual(num_len(12), 3)


if __name__ == "__main__":
    unittest.main()
