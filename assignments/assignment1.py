import unittest
import math
import random

# John O'Donnell
# Assignment 1
# due 10/31/2019


def calendar(year: int) -> list:
    # instantiate days list
    days = []

    # determine if the input year is a leap year
    leap_year = False
    if year % 4 == 0:
        leap_year = True
        if year % 100 == 0:
            leap_year = False
            if year % 400 == 0:
                leap_year = True

    # set year length predicated on leap year
    year_length = 365
    if leap_year:
        year_length = 366

    # calculate day 1
    day_jan_1 = (1 + (5 * ((year - 1) % 4)) + (4 * ((year - 1) % 100)) + (6 * ((year - 1) % 400))) % 7

    # fill the days list
    for i in range(day_jan_1, day_jan_1 + year_length):
        day_of_week = i % 7
        days.append(day_of_week)

    # lists of month names, day names, and day abbreviations
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    weekdays_full = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # determine index of the first and last days of each month
    jan_last = 30
    feb_first = jan_last + 1
    if leap_year:
        feb_last = jan_last + 29
    else:
        feb_last = jan_last + 28
    mar_first = feb_last + 1
    mar_last = feb_last + 31
    apr_first = mar_last + 1
    apr_last = mar_last + 30
    may_first = apr_last + 1
    may_last = apr_last + 31
    jun_first = may_last + 1
    jun_last = may_last + 30
    jul_first = jun_last + 1
    jul_last = jun_last + 31
    aug_first = jul_last + 1
    aug_last = jul_last + 31
    sep_first = aug_last + 1
    sep_last = aug_last + 30
    oct_first = sep_last + 1
    oct_last = sep_last + 31
    nov_first = oct_last + 1
    nov_last = oct_last + 30
    dec_first = nov_last + 1

    # instantiate a list of lists, each interior list represents a month
    month_lists = [days[:feb_first], days[feb_first:mar_first], days[mar_first:apr_first], days[apr_first:may_first],
                   days[may_first:jun_first], days[jun_first:jul_first], days[jul_first:aug_first],
                   days[aug_first:sep_first], days[sep_first:oct_first], days[oct_first:nov_first],
                   days[nov_first:dec_first], days[dec_first:]]

    print("\nIn the Year " + str(year) + ", January 1 was/will be on a " + weekdays_full[days[0]] + "\n")

    if leap_year:
        print("It is a leap year.\n")
    else:
        print("It is not a leap year.\n")

    print("     ***     CALENDAR FOR YEAR " + str(year) + "     ***\n")

    # print the months
    for i in range(0, 12):
        # print month name
        print(months[i] + "\n")
        # print weekday abbreviations
        for j in range(7):
            if j == 0:
                print(weekdays[j], end='')
            elif j < 6:
                print("  " + weekdays[j], end='')
            else:
                print("  " + weekdays[j])

        weeks = []
        this_week = []
        # fill in this_week with the next week of the month
        # add it to the weeks array
        for j in range(1, len(month_lists[i]) + 1):
            # when adding the first day of the month...
            if j == 1:
                # ensure that the first day is preceeded by empty days
                for k in range(0, month_lists[i][j - 1]):
                    this_week.append(" ")
                # add the first day
                this_week.append(j)
                # if the first day of the month is a saturday
                # add the week to the weeks list and reset this_week
                if month_lists[i][j - 1] == 6:
                    weeks.append(this_week)
                    this_week = []
            elif j == len(month_lists[i]):
                this_week.append(j)
                weeks.append(this_week)
                this_week = []
            elif month_lists[i][j - 1] < 6:
                this_week.append(j)
            elif month_lists[i][j - 1] == 6:
                this_week.append(j)
                weeks.append(this_week)
                this_week = []

        # print each week in the weeks list
        for j in range(len(weeks)):
            for k in range(len(weeks[j])):
                if weeks[j][k] == " ":
                    print("     ", end='')
                elif k == len(weeks[j]) - 1:
                    if weeks[j][k] < 10:
                        print("  " + str(weeks[j][k]))
                    else:
                        print(" " + str(weeks[j][k]))
                else:
                    if weeks[j][k] < 10:
                        print("  " + str(weeks[j][k]) + "  ", end='')
                    else:
                        print(" " + str(weeks[j][k]) + "  ", end='')

        # seperate months by blank space
        print("\n")

    return days


def alt_bubblesort(A: list, size: int) -> list:
    # instantiate a return list
    list_to_return = [A[:]]
    # as the sorted bubble grows from 0 to size - 1...
    for sorted_bubble in range(0, size - 1):
        # bubble the smallest values from the last index to the front
        i = size - 2
        while i >= sorted_bubble:
            if A[i + 1] < A[i]:
                A[i + 1], A[i] = A[i], A[i + 1]
            i -= 1
        # add the new list to the return list
        list_to_return.append(A[:])
    # after sorting, add the final list
    if size > 0:
        list_to_return.append(A[:])
    return list_to_return


def switch_bubblesort(A: list, size: int) -> list:
    left_bubble = 0     # left bubble size
    right_bubble = 0    # right bubble size
    list_to_return = [A[:]]     # return list
    iteration = 1       # iteration count

    # while the two bubbles do not account for the whole list..
    while left_bubble + right_bubble < size:
        # bubble right on second and even iterations
        if iteration % 2 == 0:
            for i in range(1 + left_bubble, size - right_bubble):
                if A[i - 1] > A[i]:
                    A[i - 1], A[i] = A[i], A[i - 1]
            iteration += 1
            right_bubble += 1
            # append list to return list
            list_to_return.append(A[:])
        # bubble left on first and odd iterations
        elif iteration % 2 == 1:
            i = size - 2 - right_bubble
            while i >= left_bubble:
                if A[i + 1] < A[i]:
                    A[i + 1], A[i] = A[i], A[i + 1]
                i -= 1
            iteration += 1
            left_bubble += 1
            # append list to return list
            list_to_return.append(A[:])
    # append the final list to the return list
    if size > 0:
        list_to_return.append(A[:])
    return list_to_return


# used to sort each bucket in bucket sort
def insertion_sort(A: list):
    # for each element of the list from index 1 to end...
    for i in range(1, len(A)):
        value = A[i]        # store value
        i_compare = i - 1   # set index to compare against
        # compare the value to each value before it
        # shift the compared values to the right if they are greater
        # insert the value once the value is compared against a smaller value
        while i_compare >= 0 and A[i_compare] > value:
            A[i_compare + 1] = A[i_compare]
            i_compare -= 1
        A[i_compare + 1] = value


def bucketsort(A: list, size:int) -> list:
    buckets = []            # establish list of buckets
    for i in range(size):   # add buckets to the bucket list
        buckets.append([])

    # for each value in the list...
    for i in range(0, len(A)):
        in_a_bucket = False
        # if the value has not yet been added to a bucket...
        while not in_a_bucket:
            # check the value against the ceiling of each bucket and
            for j in range(0, size):
                # insert the value into the first bucket with a ceiling
                # greater than the value
                if A[i] < ((j + 1) / size):
                    buckets[j].append(A[i])
                    in_a_bucket = True
                    break

    # filenames for bucket storage
    filename1 = "bucket1.txt"
    filename2 = "bucket2.txt"

    # output the unsorted buckets into a file
    first_output = open(filename1, "w")
    for bucket in buckets:
        first_output.write(str(bucket) + "\n")
    first_output.close()

    # sort each bucket individually
    for bucket in buckets:
        insertion_sort(bucket)

    # output the sorted buckets into a file
    second_output = open(filename2, "w")
    for bucket in buckets:
        second_output.write(str(bucket) + "\n")
    second_output.close()

    # concatenate the buckets into one final sorted list
    list_to_return = []
    for i in range(0, len(buckets)):
        list_to_return += buckets[i]

    return list_to_return


# get R and S values for columnsort
def getRS(N: int):
    # hardcoded case for array of length 18
    if N == 18:
        return 6, 3
    # otherwise: choose highest S and lowest R that satisfy the following
    else:
        theS = 0
        theR = 0
        for i in range(2, math.ceil(math.sqrt(N))):
            if N % i == 0:
                poss_s = i
                poss_r = int(N / i)
                if poss_r % 2 == 0:
                    if poss_r % poss_s == 0:
                        if poss_r >= (2 * poss_s**2):
                            theS = poss_s
                            theR = poss_r
        return theR, theS


# prints the columns at a given stage of columnsort
def printColumns(A: list, R: int, S: int, filename: str):
    # open file
    file_object = open(filename, "w")
    # for each element in the columns
    for element in range(R):
        # for each column
        for column in range(S):
            # in the last column, write the value and new line to file
            if column == S - 1:
                if A[column][element] is not None:
                    file_object.write(str(A[column][element]) + "\n")
                else:
                    file_object.write(" \n")
            # other wise, write the value and tab to file
            else:
                if A[column][element] is not None:
                    file_object.write(str(A[column][element]) + "\t")
                else:
                    file_object.write(" \t")
    # close file
    file_object.close()


def columnsort(A: list, N: int) -> list:
    columns = []

    # generate R and S
    R, S = getRS(N)

    # step 0
    # create columns and fill them
    for i in range(S):
        columns.append([])
    for i in range(0, len(A)):
        columns[i % S].append(A[i])
    printColumns(columns, R, S, "column1.txt")

    # step 1
    # sort the columns
    for i in range(S):
        alt_bubblesort(columns[i], len(columns[i]))
    printColumns(columns, R, S, "column2.txt")

    # step 2
    # transpose the lists
    columns_reference = []
    for i in range(S):
        columns_reference.append([])
    for i in range(S):
        for j in range(R):
            new_column = j % S
            columns_reference[new_column].append(columns[i][j])
    columns = columns_reference
    printColumns(columns, R, S, "column3.txt")

    # step 3
    # sort the columns
    for i in range(S):
        alt_bubblesort(columns[i], len(columns[i]))

    # step 4
    # inverse transpose
    columns_reference = []
    for i in range(S):
        columns_reference.append([])
    new_column = 0
    counter = 0
    for j in range(R):
        for i in range(S):
            columns_reference[new_column].append(columns[i][j])
            if counter == R - 1:
                new_column += 1
                counter = 0
            else:
                counter += 1
    columns = columns_reference

    # step 5
    # sort the columns
    for i in range(S):
        alt_bubblesort(columns[i], len(columns[i]))

    # step 6
    # shift the top half of each column into the bottom half of the same column
    # shift the bottom half of each column into the top half of the next column
    columns_reference = []
    for i in range(S + 1):
        columns_reference.append([])
    for i in range((R // 2)):
        columns_reference[0].append(None)
    for i in range(S):
        for j in range(R):
            if j < R // 2:
                columns_reference[i].append(columns[i][j])
            else:
                columns_reference[i + 1].append(columns[i][j])
    for i in range((R // 2), R):
        columns_reference[S].append(None)
    columns = columns_reference
    printColumns(columns, R, S + 1, "column4.txt")

    # step 7
    # sort the columns
    alt_bubblesort(columns[0][R // 2:], len(columns[0]) - (R // 2))
    for i in range(1, S):
        alt_bubblesort(columns[i], len(columns[i]))
    alt_bubblesort(columns[S][:R // 2], len(columns[S]) - (R // 2))

    # step 8
    # inverse column shift
    columns_reference = []
    for i in range(S):
        columns_reference.append([])
    for i in range(S):
        columns_reference[i] = columns[i][R // 2:] + columns[i + 1][:R // 2]
    columns = columns_reference

    # sorted
    # setup return list
    list_to_return = []
    for i in range(S):
        list_to_return += columns[i]

    return list_to_return


class Tests(unittest.TestCase):

    def testAltBubble(self):
        # check sorting factor and return lists
        # test for empty
        empty_list = []
        alt_bubblesort(empty_list, len(empty_list))
        self.assertListEqual(empty_list, [])
        # test for reversed list
        rev_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        alt_bubblesort(rev_list, len(rev_list))
        self.assertListEqual(rev_list, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        # test for sorted list
        sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        alt_bubblesort(sorted_list, len(sorted_list))
        self.assertListEqual(sorted_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # test for floats
        flo_list = [0, 1, 0.5, 6.1, 4, 4.444, 9.8, 3.14159, 3, 1.2]
        alt_bubblesort(flo_list, len(flo_list))
        self.assertListEqual(flo_list, [0, 0.5, 1, 1.2, 3, 3.14159, 4, 4.444, 6.1, 9.8])
        # test for repeated elements
        repeat_list = [3, 5, 2, 7, 7, 4, 3, 0, 1, 0, 3, 7]
        alt_bubblesort(repeat_list, len(repeat_list))
        self.assertListEqual(repeat_list, [0, 0, 1, 2, 3, 3, 3, 4, 5, 7, 7, 7])
        # test for negative and odd numbered list
        neg_list = [0, 44, -12, -4, 14, -110, 99]
        alt_bubblesort(neg_list, len(neg_list))
        self.assertListEqual(neg_list, [-110, -12, -4, 0, 14, 44, 99])
        # test for large numbers
        large_list = [112343, -127388, 8765690, -99234, 91235672]
        alt_bubblesort(large_list, len(large_list))
        self.assertListEqual(large_list, [-127388, -99234, 112343, 8765690, 91235672])

    def testSwitchBubble(self):
        # test partially sorted
        partsort = [1, 2, 3, 4, 6, 7, 5, 8]
        list_of_part = switch_bubblesort(partsort, len(partsort))
        self.assertListEqual(partsort, [1, 2, 3, 4, 5, 6, 7, 8])
        # test empty
        empty_list = []
        list_of_lists = [[]]
        list_of_empties = switch_bubblesort(empty_list, len(empty_list))
        self.assertListEqual(empty_list, [])
        self.assertListEqual(list_of_lists, list_of_empties)
        # test for reversed list odd number
        rev_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        list_of_lists = [[9, 8, 7, 6, 5, 4, 3, 2, 1],
                         [1, 9, 8, 7, 6, 5, 4, 3, 2],
                         [1, 8, 7, 6, 5, 4, 3, 2, 9],
                         [1, 2, 8, 7, 6, 5, 4, 3, 9],
                         [1, 2, 7, 6, 5, 4, 3, 8, 9],
                         [1, 2, 3, 7, 6, 5, 4, 8, 9],
                         [1, 2, 3, 6, 5, 4, 7, 8, 9],
                         [1, 2, 3, 4, 6, 5, 7, 8, 9],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        rev_list_list = switch_bubblesort(rev_list, len(rev_list))
        self.assertListEqual(rev_list, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertListEqual(rev_list_list, list_of_lists)
        # test for reversed list even number
        rev_list = [8, 7, 6, 5, 4, 3, 2, 1]
        list_of_lists = [[8, 7, 6, 5, 4, 3, 2, 1],
                         [1, 8, 7, 6, 5, 4, 3, 2],
                         [1, 7, 6, 5, 4, 3, 2, 8],
                         [1, 2, 7, 6, 5, 4, 3, 8],
                         [1, 2, 6, 5, 4, 3, 7, 8],
                         [1, 2, 3, 6, 5, 4, 7, 8],
                         [1, 2, 3, 5, 4, 6, 7, 8],
                         [1, 2, 3, 4, 5, 6, 7, 8],
                         [1, 2, 3, 4, 5, 6, 7, 8],
                         [1, 2, 3, 4, 5, 6, 7, 8]]
        rev_list_list = switch_bubblesort(rev_list, len(rev_list))
        self.assertListEqual(rev_list, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertListEqual(rev_list_list, list_of_lists)
        # test for sorted list
        sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        switch_bubblesort(sorted_list, len(sorted_list))
        self.assertListEqual(sorted_list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # test for floats
        flo_list = [0, 1, 0.5, 6.1, 4, 4.444, 9.8, 3.14159, 3, 1.2]
        switch_bubblesort(flo_list, len(flo_list))
        self.assertListEqual(flo_list, [0, 0.5, 1, 1.2, 3, 3.14159, 4, 4.444, 6.1, 9.8])
        # test for repeated elements
        repeat_list = [3, 5, 2, 7, 7, 4, 3, 0, 1, 0, 3, 7]
        switch_bubblesort(repeat_list, len(repeat_list))
        self.assertListEqual(repeat_list, [0, 0, 1, 2, 3, 3, 3, 4, 5, 7, 7, 7])
        # test for negative and odd numbered list
        neg_list = [0, 44, -12, -4, 14, -110, 99]
        switch_bubblesort(neg_list, len(neg_list))
        self.assertListEqual(neg_list, [-110, -12, -4, 0, 14, 44, 99])
        # test for large numbers
        large_list = [112343, -127388, 8765690, -99234, 91235672]
        switch_bubblesort(large_list, len(large_list))
        self.assertListEqual(large_list, [-127388, -99234, 112343, 8765690, 91235672])

    @unittest.skip
    def testBucket(self):
        raise NotImplementedError

    def testColumn(self):
        # test the given array, len 18
        given = [10, 14, 5, 8, 7, 17, 12, 1, 6, 16, 9, 11, 4, 15, 2, 18, 3, 13]
        givenColumn = columnsort(given, len(given))
        given.sort()
        self.assertListEqual(givenColumn, given)

        # test a random array, len 36
        test36 = []
        for i in range(36):
            test36.append(random.randint(-50, 50))
        test36Column = columnsort(test36, len(test36))
        test36.sort()
        self.assertListEqual(test36Column, test36)

        # test a random array, len 48
        test48 = []
        for i in range(48):
            test48.append(random.randint(-50, 50))
        test48Column = columnsort(test48, len(test48))
        test48.sort()
        self.assertListEqual(test48Column, test48)

        # test a random array, len 72
        test72 = []
        for i in range(72):
            test72.append(random.randint(-50, 50))
        test72Column = columnsort(test72, len(test72))
        test72.sort()
        self.assertListEqual(test72Column, test72)


def main():
    return


if __name__ == "__main__":
    # unittest.main()
    main()
