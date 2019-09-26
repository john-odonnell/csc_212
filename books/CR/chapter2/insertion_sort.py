# array assignment
a = [31, 41, 59, 26, 41, 58]    # establish array
print(a)                        # print initial array

for index in range(1, len(a)):  # for index from range 1 to the length of the array

    value = a[index]            # store value at the index
    index_compare = index - 1   # the comparative index is one less than the index

    while index_compare >= 0 and a[index_compare] > value:  # while the comparative index >= 0 and the value at the
                                                            # index being stored is greater than the value being compared

        a[index_compare + 1] = a[index_compare]   # store the comparative value in the index of the value being compared
        index_compare -= 1                        # increment the comparative index leftwards

    a[index_compare + 1] = value                            # otherwise, store the value above the comparative index

print(a)    # print sorted array

# in real world terms:
# the first value remains in its spot
# the second value is compared to the first, and switched if its lower
# the third value is compared to the second, and so on and so forth

# sorted in place, which requires no extra data storage

# in general, running time is a function of input size
# typically, each basic operation i take a constant amount of time ci
