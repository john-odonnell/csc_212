# find the iterative factorial
# find the recursive factorial


def iterative_factorial(n):
    n_factorial = 1
    for i in range(1, n + 1):
        n_factorial *= i
    return n_factorial


def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


def iterative_power(a, b):
    total = 1
    for i in range(0, b):
        total *= a
    return total


def recursive_power(a, b):
    if b == 1:
        return a
    # if b == 0:
        # return 1
    else:
        return a * recursive_power(a, b - 1)


def main():
    print(iterative_factorial(5))
    print(recursive_factorial(5))
    print(iterative_power(2, 5))
    print(recursive_power(2, 5))


main()
