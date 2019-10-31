# list = [4, 1, 19, 18, 10, 3, 7, 9, 1, 0, 2]
# childL = 2 * i + 1
# childR = 2 * i + 2
# parentL = floor(i/2)
# parentR = floor(i/2) - 1

import unittest


def left(i: int) -> int:
    """ Returns the index of the left-child of the given index.
    """
    index = (2 * i) + 1
    return index


def right(i: int) -> int:
    """ Returns the index of the right-child of the given index.
    """
    index = (2 * i) + 2
    return index


def parent(i: int) -> int:
    """ Returns the parent index of the index given.
    """
    if i % 2 == 1:
        index = i // 2
    else:
        index = (i // 2) - 1
    return index


def heapify(A: list, i: int) -> list:
    """ Transform the given list into a heap and then return it.
    You should use the left, right and parent functions.
    This method should run recursively.
    """
    if left(i) > len(A) - 1:

        return A
    elif left(i) == len(A) - 1:
        if A[left(i)] > A[i]:
            A[left(i)], A[i] = A[i], A[left(i)]
            heapify(A, left(i))

        return A
    else:
        if A[left(i)] > A[i] and A[left(i)] >= A[right(i)]:
            A[left(i)], A[i] = A[i], A[left(i)]
            heapify(A, left(i))
        elif A[right(i)] > A[i] and A[right(i)] > A[left(i)]:
            A[right(i)], A[i] = A[i], A[right(i)]
            heapify(A, right(i))

        return A


def build_max_heap(A: list) -> list:
    """ Build a max heap here.
    Do this by converting the input list into a heap and return it.
    This method should run iteratively to create the final heap.
    """
    i = parent(len(A) - 1)
    while i >= 0:
        A = heapify(A, i)
        i -= 1
    return A


def heapsort(A: list) -> list:
    """ HeapSorts a given list.
    This method should run iteratively.
    """
    A = build_max_heap(A)
    i = len(A) - 1
    while i >= 0:
        A[i], A[0] = A[0], A[i]
        unsorted = heapify(A[:i], 0)
        A = unsorted + A[i:]
        i -= 1
    return A


class Tests(unittest.TestCase):
    def test_heapify(self):
        """ Does your heapify method work?
        The first tests for a sorted list.
        Since the heapify function heapifies subtrees,
        this will not return the same, sorted list
        """
        # list
        list = [1, 18, 10, 9, 1, 0, 2]
        list_heaped = heapify(list, 0)
        self.assertListEqual(list_heaped, [18, 9, 10, 1, 1, 0, 2])

        list = [4, 18, 19, 9, 10, 3, 7, 1, 1, 0, 2]
        list_heaped = heapify(list, 0)
        self.assertListEqual(list_heaped, [19, 18, 7, 9, 10, 3, 4, 1, 1, 0, 2])

        list = [19, 1, 7, 18, 10, 3, 4, 9, 1, 0, 2]
        list_heaped = heapify(list, 1)
        self.assertListEqual(list_heaped, [19, 18, 7, 9, 10, 3, 4, 1, 1, 0, 2])

    def test_buildmaxheap(self):
        """ Does your max heap method work?
        These should not test for a sorted list,
        but instead for a max heap represented as a list.
        """
        # list
        list = [4, 1, 19, 18, 10, 3, 7, 9, 1, 0, 2]
        list_maxheap = build_max_heap(list)
        self.assertListEqual(list_maxheap, [19, 18, 7, 9, 10, 3, 4, 1, 1, 0, 2])
        # with negatives
        list = [3, 6, 5, 8, 9, -12, 0, -3, -7, 4, 4, -9]
        list_maxheap = build_max_heap(list)
        self.assertListEqual(list_maxheap, [9, 8, 5, 3, 6, -9, 0, -3, -7, 4, 4, -12])
        # repeated elements
        list = [38, 41, 50, 12, 3, 26, 19, 50, 35]
        list_maxheap = build_max_heap(list)
        self.assertListEqual(list_maxheap, [50, 41, 50, 38, 3, 26, 19, 12, 35])

    def test_heapsort(self):
        """ Does heapsort work?
        """
        # Hand-made case: duplicate and change as you need to debug.
        A = [1, 2, 3, 4, 5]
        self.assertListEqual(sorted(A), heapsort(A))
        # reverse
        A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertListEqual(sorted(A), heapsort(A))
        # Random case: change the range of numbers and length as you see fit.
        import random
        A = [random.randint(-50, 50) for _ in range(15)]
        self.assertListEqual(sorted(A), heapsort(A))
        return


if __name__ == "__main__":
    unittest.main()
