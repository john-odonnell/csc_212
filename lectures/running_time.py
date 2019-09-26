import time


def SumOfN(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum += i
    end = time.time()

    return theSum, end-start


def directSumOfN(n):
    start = time.time()
    theSum = ((n*(n+1))/2)
    end = time.time()

    return theSum, end-start


print("---Computes the sum of all numbers up to N---")
number = int(input("Input value for N: "))

print("Loop Sum Results: ")
for i in range(0, 5):
    loop_sum, loop_time = SumOfN(number)
    print("\tSum: ", str(loop_sum), "\tRun Time: ", str(loop_time))
print("Direct Sum Results: ")
for i in range(0, 5):
    direct_sum, direct_time = directSumOfN(number)
    print("\tSum: ", str(direct_sum), "\tRun Time: ", str(direct_time))