import unittest
from typing import Union


def insertion_sort(A: list) -> list:
    for i in range(1, len(A)):
        value = A[i]
        j = i - 1
        while j >= 0 and value < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = value
    return A


def check_sort(A: list) -> list:
    """ Create a function which checks if a list is sorted.
    If it is not sorted then sort the function using insertion sort
    """

    i = 1
    checking = True
    while checking and i < len(A):
        if A[i] < A[i - 1]:
            insertion_sort(A)
            checking = False
        i += 1
    return A


def it_bin_search(A: list, x: int) -> Union[int, None]:
    """ Create an iterative binary search function. Remember to use check_sort

    as a helper function. In order for binary search to work the list must be sorted
    A is a list. x is an element that you are searching for in the list
    """
    A = check_sort(A)

    right = len(A)
    left = 0
    mid = (right + left) // 2

    while A[mid] != x:
        if A[mid] < x:
            left = mid
            mid = (right + left) // 2
        elif A[mid] > x:
            right = mid
            mid = (right + left) // 2
        elif right == left + 1 or right == left:
            return None

    return mid


def rc_bin_search(A: list, l: int, r: int, x: int) -> Union[int, None]:
    """ Create a recursive binary search function.

    A is a list, l is the left most element in the list, r is the right most element,
    and x is the element you are searching for.
    """
    A = check_sort(A)

    if l == r:
        return None
    else:
        mid = (r + l) // 2
        if A[mid] == x:
            return mid
        if A[mid] < x:
            return rc_bin_search(A, mid, r, x)
        if A[mid] > x:
            return rc_bin_search(A, l, mid, x)


class TestCases(unittest.TestCase):
    """ Property-Based Testing.
    The testcase you see below uses 'property-based testing' techniques.
    Essentially, you specify the inputs and what properties the outputs
    *should* have, such as being sorted. Hypothesis will search the
    entire universe of possible inputs, in an attempt to break your code.
    Property-based testing is one of the most thorough ways to test your
    code, though it won't always be applicable. Use it whenever you can.
    Uncomment this block to use this test case, to install hypothesis run:
    python3 -m pip install hypothesis
    """

    from hypothesis import strategies as st, given

    @given(st.lists(st.integers()))
    def test_check_sort(self, A):
        self.assertListEqual(sorted(A), check_sort(A))
        return

    #@given(st.lists(st.integers()))
    #def test_bin_searches(self, A):
    #    self.assertListEqual(it_bin_search(A, 7), rc_bin_search(A, 0, len(A) - 1, 7))
    #    return

    def test_check(self):
        sorted = [1, 2, 3, 4, 5]
        self.assertListEqual(check_sort(sorted), [1, 2, 3, 4, 5])
        unsorted = [5, 4, 6, 3, 8, 2]
        self.assertListEqual(check_sort(unsorted), [2, 3, 4, 5, 6, 8])
        reverse = [7, 6, 5, 4, 3, 2, 1]
        self.assertListEqual(check_sort(reverse), [1, 2, 3, 4, 5, 6, 7])

    def test_it_bin(self):
        sorted = [12, 5, 4, 6, 8, 3, 9, 0, 4, 6, 8]
        index = it_bin_search(sorted, 9)
        self.assertEqual(index, 9)
        unsorted = [5, 4, 6, 3, 8, 2]
        index = it_bin_search(unsorted, 6)
        self.assertEqual(index, 4)
        reverse = [7, 6, 5, 4, 3, 2, 1]
        index = it_bin_search(reverse, 5)
        self.assertEqual(index, 4)

    def test_rc_bin(self):
        sorted = [12, 5, 4, 6, 8, 3, 9, 0, 4, 6, 8]
        # sorted = [0, 3, 4, 4, 5, 6, 6, 8, 8, 9, 12]
        index = rc_bin_search(sorted, 0, len(sorted) - 1, 9)
        self.assertEqual(index, 9)
        unsorted = [5, 4, 6, 3, 8, 2]
        index = rc_bin_search(unsorted, 0, len(unsorted) - 1, 6)
        self.assertEqual(index, 4)
        reverse = [7, 6, 5, 4, 3, 2, 1]
        index = rc_bin_search(reverse, 0, len(reverse) - 1, 5)
        self.assertEqual(index, 4)


if __name__ == "__main__":
    unittest.main()