binary_one = [1, 1, 0, 1]   # store binary to
binary_two = [1, 0, 0, 1]   # be added
print(binary_one)           # display
print(binary_two)           # for clarity

binary_sum = [0, 0, 0, 0, 0]    # instantiate binary sum array

length = len(binary_one)    # in order to loop through the array backwards,
index = length - 1          # find the length of the arrays and sub 1

next_digit_store = 0    # int value to store data for digit carrying

while index >= -1:
    if index >= 0:
        if binary_one[index] + binary_two[index] + next_digit_store == 0:
            binary_sum[index + 1] = 0
            next_digit_store = 0
        elif binary_one[index] + binary_two[index] + next_digit_store == 1:
            binary_sum[index + 1] = 1
            next_digit_store = 0
        elif binary_one[index] + binary_two[index] + next_digit_store == 2:
            binary_sum[index + 1] = 0
            next_digit_store = 1
        elif binary_one[index] + binary_two[index] + next_digit_store == 3:
            binary_sum[index + 1] = 1
            next_digit_store = 1
    else:
        binary_sum[index + 1] = next_digit_store
    index -= 1

print(binary_sum)
