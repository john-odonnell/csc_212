import unittest
import random


def partition(A: list, p: int, r: int) -> int:
    """ Lomuto Partition.
    :param A: an unsorted list.
    :param p: the index of the leftmost element
    :param r: one larger than the index of the rightmost element
    :return the index of the pivot in A
    """

    # pivot is the index of the last element in the list
    too_big = p
    pivot = r - 1
    too_small = pivot - 1

    while too_small >= too_big:
        while too_small >= too_big and A[too_big] <= A[pivot]:
            too_big += 1
        while A[too_small] > A[pivot] and too_small >= too_big:
            too_small -= 1
        if too_big < too_small:
            A[too_big], A[too_small] = A[too_small], A[too_big]
    A[pivot], A[too_big] = A[too_big], A[pivot]
    sorted_index = too_big

    return sorted_index


def quicksort(A: list) -> list:
    """ Recursive Quicksort.
    :param A: an unsorted list.
    """
    if len(A) == 0 or len(A) == 1:
        return A
    else:
        pivot = partition(A, 0, len(A))

        L = quicksort(A[:pivot])
        R = quicksort(A[pivot + 1:])

        A[:pivot] = L
        A[pivot + 1:] = R

        return A


def rand_partition(A: list, p: int, r: int) -> int:
    """ Random Partitioning.
    :param A: an unsorted list
    :param p: the index of the leftmost element
    :param r: one larger than the index of the rightmost element
    """
    pivot = random.randint(p, r)
    if pivot != r - 1:
        A[pivot], A[r - 1] = A[r - 1], A[pivot]
        pivot = r - 1

    too_big = p
    too_small = pivot - 1

    while too_small >= too_big:
        while too_small >= too_big and A[too_big] <= A[pivot]:
            too_big += 1
        while A[too_small] > A[pivot] and too_small >= too_big:
            too_small -= 1
        if too_big < too_small:
            A[too_big], A[too_small] = A[too_small], A[too_big]
    A[pivot], A[too_big] = A[too_big], A[pivot]
    sorted_index = too_big

    return sorted_index


def rand_quicksort(A: list) -> list:
    """ Randomized Quicksort.
    :param A: an unsorted list.
    """

    if len(A) == 0 or len(A) == 1:
        return A
    else:
        pivot = rand_partition(A, 0, len(A))

        L = rand_quicksort(A[:pivot])
        R = rand_quicksort(A[pivot + 1:])

        A[:pivot] = L
        A[pivot + 1:] = R

        return A


class Tests(unittest.TestCase):
    """ Unit tests for Quicksort.
    Add your own unit tests as you complete each section.
    """

    def test_partition(self):
        """Test 1 - Basic"""
        A = [10, 20, 50, 40, 30]
        pivot = partition(A, 0, len(A))
        self.assertEqual(pivot, 2)
        self.assertTrue(all([x < A[pivot] for x in A[:pivot]]))
        self.assertTrue(all([x >= A[pivot] for x in A[pivot:]]))

        """Test 2 - Basic"""
        B = [50, 40, 10, 20, 30]
        pivot = partition(B, 0, len(B))
        self.assertEqual(pivot, 2)
        self.assertTrue(all([x < B[pivot] for x in B[:pivot]]))
        self.assertTrue(all([x >= B[pivot] for x in B[pivot:]]))

        """Test 3 - Negatives"""
        C = [-16, 23, -2, -5, 76, 50]
        pivot = partition(C, 0, len(C))
        self.assertEqual(pivot, 4)
        self.assertTrue(all([x < C[pivot] for x in C[:pivot]]))
        self.assertTrue(all([x >= C[pivot] for x in C[pivot:]]))

        """Test 4 - Repeated Elements"""
        D = [7, 2, 5, 2, 4, 2, 3]
        pivot = partition(D, 0, len(D))
        self.assertEqual(pivot, 3)
        self.assertTrue(all([x < D[pivot] for x in D[:pivot]]))
        self.assertTrue(all([x >= D[pivot] for x in D[pivot:]]))

        """Test 5 - Subset
        -testing to see that partition works on a subset of our list
        -(necessary for quicksort to work properly)
        -only the sublist [3, 7, 5] should be partitioned, with
         other elements in our full list remaining the same
        """
        E = [10, 3, 7, 5, 0]
        pivot = partition(E, 1, len(E)-1)
        self.assertEqual(pivot, 2)
        self.assertListEqual(E, [10, 3, 5, 7, 0])

    def test_quicksort(self):
        A = [10, 20, 50, 40, 30]
        quicksort(A)
        self.assertListEqual(A, [10, 20, 30, 40, 50])

        B = [50, 40, 10, 20, 30]
        quicksort(B)
        self.assertListEqual(B, [10, 20, 30, 40, 50])

        C = [-16, 23, -2, -5, 76, 50]
        quicksort(C)
        self.assertListEqual(C, [-16, -5, -2, 23, 50, 76])

        D = [7, 2, 5, 2, 4, 2, 3]
        quicksort(D)
        self.assertListEqual(D, [2, 2, 2, 3, 4, 5, 7])

        E = [10, 3, 7, 5, 0]
        quicksort(E)
        self.assertListEqual(E, [0, 3, 5, 7, 10])

    def test_rand_partition(self):
        """Test 1 - Basic"""
        A = [10, 20, 50, 40, 30]
        pivot = rand_partition(A, 0, len(A))
        self.assertTrue(all([x < A[pivot] for x in A[:pivot]]))
        self.assertTrue(all([x >= A[pivot] for x in A[pivot:]]))

        """Test 2 - Basic"""
        B = [50, 40, 10, 20, 30]
        pivot = rand_partition(B, 0, len(B))
        self.assertTrue(all([x < B[pivot] for x in B[:pivot]]))
        self.assertTrue(all([x >= B[pivot] for x in B[pivot:]]))

        """Test 3 - Negatives"""
        C = [-16, 23, -2, -5, 76, 50]
        pivot = rand_partition(C, 0, len(C))
        self.assertTrue(all([x < C[pivot] for x in C[:pivot]]))
        self.assertTrue(all([x >= C[pivot] for x in C[pivot:]]))

        """Test 4 - Repeated Elements"""
        D = [7, 2, 5, 2, 4, 2, 3]
        pivot = rand_partition(D, 0, len(D))
        self.assertTrue(all([x < D[pivot] for x in D[:pivot]]))
        self.assertTrue(all([x >= D[pivot] for x in D[pivot:]]))

        """Test 5 - Subset
        -testing to see that partition works on a subset of our list
        -(necessary for quicksort to work properly)
        -only the sublist [3, 7, 5] should be partitioned, with
         other elements in our full list remaining the same
        """
        E = [10, 3, 7, 5, 0]
        pivot = rand_partition(E, 1, len(E) - 1)
        self.assertTrue(all([x < E[pivot] for x in E[1:pivot]]))
        self.assertTrue(all([x >= E[pivot] for x in E[pivot:len(E) - 1]]))

    def test_rand_quicksort(self):
        A = [10, 20, 50, 40, 30]
        rand_quicksort(A)
        self.assertListEqual(A, [10, 20, 30, 40, 50])

        B = [50, 40, 10, 20, 30]
        rand_quicksort(B)
        self.assertListEqual(B, [10, 20, 30, 40, 50])

        C = [-16, 23, -2, -5, 76, 50]
        rand_quicksort(C)
        self.assertListEqual(C, [-16, -5, -2, 23, 50, 76])

        D = [7, 2, 5, 2, 4, 2, 3]
        rand_quicksort(D)
        self.assertListEqual(D, [2, 2, 2, 3, 4, 5, 7])

        E = [10, 3, 7, 5, 0]
        rand_quicksort(E)
        self.assertListEqual(E, [0, 3, 5, 7, 10])


if __name__ == "__main__":
    unittest.main()
