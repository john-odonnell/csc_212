a = [31, 41, 59, 26, 41, 58]
v = 41
i = []

# input: array a, value v
# output: index i of value v, or NIL if nonexistent

for i_check in range(0, len(a)):
    v_check = a[i_check]
    if v_check == v:
        i.append(i_check)

if i:
    print("The value is stored at: " + str(i))
else:
    print("The value is not stored in the array.")

# LOOP INVARIANT:
# At the start of each iteration of the for loop of lines 8-11,
# the subarray a[1..i_check] has been searched for the value v,
# and if found the index of said value has been stored in an external array

# INITIALIZATION:
# prior to the first iteration of the loop, the subarray a[0] has been searched
# for value v, and if found it has been added to the external array

# MAINTENANCE:
# this fact maintains through the whole array

# TERMINATION:
# the entire array has been searched, and the indecies corresponding to the value
# have been stored in the external array