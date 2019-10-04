def num_to_string(n, base):
    conversion_string = "0123456789ABCDEF"

    if n < base:
        return conversion_string[n]
    else:
        this_digit = n % base
        n = int(n / base)
        return conversion_string[this_digit] + num_to_string(n, base)


def main():
    num = int(input("Input number to convert: "))
    base = int(input("Input base: "))

    converted_string = num_to_string(num, base)
    print(converted_string)


main()
