import unittest
import math
import random


def calendar() -> list:
    year = int(input("Enter year: "))
    days = []

    leap_year = False
    if year % 4 == 0:
        leap_year = True
        if year % 100 == 0:
            leap_year = False
            if year % 400 == 0:
                leap_year = True

    year_length = 365
    if leap_year:
        year_length = 366

    day_jan_1 = (1 + (5 * ((year - 1) % 4)) + (4 * ((year - 1) % 100)) + (6 * ((year - 1) % 400))) % 7

    for i in range(day_jan_1, day_jan_1 + year_length):
        day_of_week = i % 7
        days.append(day_of_week)

    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    weekdays_full = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

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

    for i in range(0, 12):
        print(months[i] + "\n")
        for j in range(7):
            if j == 0:
                print(weekdays[j], end='')
            elif j < 6:
                print("  " + weekdays[j], end='')
            else:
                print("  " + weekdays[j])

        weeks = []
        this_week = []
        for j in range(1, len(month_lists[i]) + 1):
            if j == 1:
                for k in range(0, month_lists[i][j - 1]):
                    this_week.append(" ")
                this_week.append(j)
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

        print("\n")

    return days


def alt_bubblesort(A: list, size: int) -> list:
    list_to_return = [A[:]]
    for sorted_bubble in range(0, size - 1):
        i = size - 2
        while i >= sorted_bubble:
            if A[i + 1] < A[i]:
                A[i + 1], A[i] = A[i], A[i + 1]
            i -= 1
        list_to_return.append(A[:])
    list_to_return.append(A[:])
    return list_to_return


def switch_bubblesort(A: list, size: int) -> list:
    left_bubble = 0
    right_bubble = 0
    list_to_return = [A[:]]
    iteration = 1
    while left_bubble + right_bubble < size - 1:
        if iteration % 2 == 1:
            for i in range(1 + left_bubble, size - right_bubble):
                if A[i - 1] > A[i]:
                    A[i - 1], A[i] = A[i], A[i - 1]
            iteration += 1
            right_bubble += 1
            list_to_return.append(A[:])
        elif iteration % 2 == 0:
            i = size - 2 - right_bubble
            while i >= left_bubble:
                if A[i + 1] < A[i]:
                    A[i + 1], A[i] = A[i], A[i + 1]
                i -= 1
            iteration += 1
            left_bubble += 1
            list_to_return.append(A[:])
    list_to_return.append(A[:])
    return list_to_return


def insertion_sort(A: list):
    for i in range(1, len(A)):
        value = A[i]
        i_compare = i - 1
        while i_compare >= 0 and A[i_compare] > value:
            A[i_compare + 1] = A[i_compare]
            i_compare -= 1
        A[i_compare + 1] = value


def bucketsort(A: list, size:int) -> list:
    buckets = []
    for i in range(0, size):
        buckets.append([])

    bucket_ceilings = []
    current_ceiling = 0
    for i in range(0, len(buckets) - 1):
        current_ceiling += 1 / size
        bucket_ceilings.append(current_ceiling)
    bucket_ceilings.append(1)

    print(bucket_ceilings)

    for i in range(0, len(A)):
        in_a_bucket = False
        while not in_a_bucket:
            for j in range(0, len(bucket_ceilings)):
                if j == 0:
                    if A[i] <= bucket_ceilings[j]:
                        buckets[j].append(A[i])
                        in_a_bucket = True
                else:
                    if bucket_ceilings[j - 1] < A[i] <= bucket_ceilings[j]:
                        buckets[j].append(A[i])
                        # A[i] = 2.0
                        in_a_bucket = True

    filename1 = "bucket1.txt"
    filename2 = "bucket2.txt"

    first_output = open(filename1, "w")
    for bucket in buckets:
        first_output.write(str(bucket) + "\n")
    first_output.close()

    for bucket in buckets:
        insertion_sort(bucket)

    second_output = open(filename2, "w")
    for bucket in buckets:
        second_output.write(str(bucket) + "\n")
    second_output.close()

    list_to_return = []
    for i in range(0, len(buckets)):
        list_to_return += buckets[i]
    return list_to_return


# diffuse into functions or simplify into less loops
# also replace len calls with R and S
def columnsort(A: list, N: int) -> list:
    columns = []
    R = 0
    S = 0

    for i in range(0, math.sqrt(N)):
        if N % i == 0:
            possibleS = i
            possibleR = N / i
            if possibleR % 2 == 0:
                if possibleR % possibleS == 0:
                    if R >= (2 * possibleS**2):
                        R = possibleR
                        S = possibleS

    for i in range(0, S):
        columns.append([])
    for i in range(0, len(A)):
        column = i % S
        columns[column].append(A[i])

    for i in range(0, len(columns)):
        switch_bubblesort(columns[i], len(columns[i]))

    columns_reference = columns[:]
    for i in range(0, len(columns_reference)):
        new_index = -1
        for j in range(0, len(columns_reference[i])):
            new_column = j % S
            if j % S == 0:
                j += 1
            columns[new_column[new_index]] = columns_reference[i][j]

    for i in range(0, len(columns)):
        switch_bubblesort(columns[i], len(columns[i]))

    for i in range(0, len(columns[0])):
        new_column = -1
        new_index = -1
        # for j in range(0, len(columns)):







def main():
    this_list = [6, 10, 3, 9, 4, 8, 7, 1]
    print(alt_bubblesort(this_list, len(this_list)))
    print("\n")

    this_list = [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(switch_bubblesort(this_list, len(this_list)))
    print("\n")

    bucketsort_list = [0.1, 0.6, 0.4, 0.5, 0.9, 0.3, 0.2, 0.7, 0.8]
    bucketsort(bucketsort_list, 3)

    calendar()


main()
