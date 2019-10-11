def bubbleSort(array: list):
    for sorted_bubble in range(0, len(array) - 1):
        for i in range(1, len(array) - sorted_bubble):
            if array[i-1] > array[i]:
                larger_value = array[i-1]
                array[i-1] = array[i]
                array[i] = larger_value


def forwards_bubble(array:list):
    for sorted_bubble in range(0, len(array) - 1):
        i = len(array) - 2
        while i >= sorted_bubble:
            if array[i + 1] < array[i]:
                array[i + 1], array[i] = array[i], array[i + 1]
            i -= 1


def bothways_bubble(array:list):
    left_bubble = 0
    right_bubble = 0
    while left_bubble + right_bubble < len(array) - 1:
        iteration = 1
        if iteration % 2 == 1:
            for i in range(1 + left_bubble, len(array) - right_bubble):
                if array[i - 1] > array[i]:
                    array[i - 1], array[i] = array[i], array[i - 1]
            iteration += 1
            right_bubble += 1
        elif iteration % 2 == 0:
            i = len(array) - 2 - right_bubble
            while i >= left_bubble:
                if array[i + 1] < array[i]:
                    array[i + 1], array[i] = array[i], array[i + 1]
                i -= 1
            iteration += 1
            left_bubble += 1


print("Backwards Bubble:")
int_list = [100, 23, 5, 77, 92, 0]
print(int_list)
bubbleSort(int_list)
print(int_list)

print("Forwards Bubble:")
int_list = [111, 112, 0, 0, 4, 34, 55]
print(int_list)
forwards_bubble(int_list)
print(int_list)

print("Converging Bubbles:")
int_list = [566, 43, 55, 44, 0, 1, 1, 17, 77]
print(int_list)
bothways_bubble(int_list)
print(int_list)
