import unittest
from functools import reduce
from random import randint
from typing import List
import argparse


def merge(A: list, mid: int) -> None:
    """ Merges the two inner lists contained within A.
    A is comprised of two sorted lists, from A[0] to A[mid - 1],
    and A[mid], A[len(A) - 1]. This function combines these two lists,
    directly modifying the contents in A such that, upon return,
    it is sorted.
    """
    B = A[:]
    pointL = 0
    pointR = mid
    for i in range(0, len(A)):
        if pointL == mid:
            A[i] = B[pointR]
            pointR += 1
        elif pointR == len(A):
            A[i] = B[pointL]
            pointL += 1
        elif B[pointL] <= B[pointR]:
            A[i] = B[pointL]
            pointL += 1
        else:
            A[i] = B[pointR]
            pointR += 1
    del B
    return


def Mergesort(A: list) -> None:
    """ Sorts the given list using Mergesort. """
    print(A)
    if len(A) <= 1:
        return
    else:
        mid = len(A)//2

        Mergesort(A[:mid])
        Mergesort(A[mid:])

        merge(A, mid)
        print(A)

        return

def MergesortPlus(A: list) -> None:
    """ Sorts the given list using an improved Mergesort. """
    # TODO
    pass


class Tests(unittest.TestCase):

    def test_merge(self):
        # test for large numbers
        listbig = [13242424, 329483943, 23237273, 934090340]
        merge(listbig, 2)
        self.assertListEqual(listbig, [13242424, 23237273, 329483943, 934090340])
        # test for floats
        listdec = [0.2, 0.5, 0.9, 0.1, 0.3, 0.8]
        merge(listdec, 3)
        self.assertListEqual(listdec, [0.1, 0.2, 0.3, 0.5, 0.8, 0.9])
        # test for repeated elements
        listrep = [0, 1, 2, 3, 1, 1, 2, 6]
        merge(listrep, 4)
        self.assertListEqual(listrep, [0, 1, 1, 1, 2, 2, 3, 6])
        # test for negatives
        listnega = [-1, 17, -18, 2]
        merge(listnega, 2)
        self.assertListEqual(listnega, [-18, -1, 2, 17])
        # test for list with odd number of elements
        listodd = [1, 4, 5, 2, 3]
        merge(listodd, 3)
        self.assertListEqual(listodd, [1, 2, 3, 4, 5])
        # test for list of 1 element
        listone = [7]
        merge(listone, 0)
        self.assertListEqual(listone, [7])
        # test for list with lopsided mid
        listlop = [1, 16, 33, 49, 65, 81, 97, 2, 17, 34]
        merge(listlop, 7)
        self.assertListEqual(listlop, [1, 2, 16, 17, 33, 34, 49, 65, 81, 97])

    def test_mergesort(self):
        """ Does Mergesort work? """
        # test for large numbers
        listbig = [13242424, 329483943, 23237273, 934090340]
        Mergesort(listbig)
        self.assertListEqual(listbig, [13242424, 23237273, 329483943, 934090340])
        # test for floats
        listdec = [0.2, 0.5, 0.9, 0.1, 0.3, 0.8]
        Mergesort(listdec)
        self.assertListEqual(listdec, [0.1, 0.2, 0.3, 0.5, 0.8, 0.9])
        # test for repeated elements
        listrep = [0, 1, 2, 3, 1, 1, 2, 6]
        Mergesort(listrep)
        self.assertListEqual(listrep, [0, 1, 1, 1, 2, 2, 3, 6])
        # test for negatives
        listnega = [-1, 17, -18, 2]
        Mergesort(listnega)
        self.assertListEqual(listnega, [-18, -1, 2, 17])
        # test for list with odd number of elements
        listodd = [1, 7, 5, 3, 2]
        Mergesort(listodd)
        self.assertListEqual(listodd, [1, 2, 3, 5, 7])
        # test for a long list with odd number of elements
        listoddlong = [1, 3, 5, 2, 4, 7, 8, 2, 4, 5, 9, 1, 0, 2, 3]
        Mergesort(listoddlong)
        self.assertListEqual(listoddlong, [0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 7, 8, 9])
        # test for list of 1 element
        listone = [7]
        Mergesort(listone)
        self.assertListEqual(listone, [7])


    @unittest.skip
    def test_mergesort_plus(self):
        """ Does MergesortPlus work? """
        # TODO
        raise NotImplementedError

    @unittest.skip
    def test_mergesort_vs_mergesortplus(self):
        """ Benchmark performance of Mergesort vs MergesortPlus. """
        # TODO
        raise NotImplementedError

    @staticmethod
    def isSorted(A: list) -> bool:
        """ A helper method to determine if a list is sorted. """
        return all([a <= b for (a, b) in zip(A, A[1:])])

    @staticmethod
    def randomList(n: int = 1_000) -> List[int]:
        """ Generates and returns a list of random numbers in the range (-n, n) of length n. """
        return [randint(-n, n) for _ in range(n)]


if __name__ == "__main__":
    unittest.main()