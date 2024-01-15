# Given an integer, n, print the following values for each integer i from 1 to n:
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary

# Prints: The four values must be printed on a single line in the order specified above for each i from 1 to . Each
# value should be space-padded to match the width of the binary value of number and the values should be separated by a
# single space.

def print_formatted(number):
    width = len(str(bin(number)[2:]))

    for i in range(1, number + 1):
        print(str(i).rjust(width, ' '), str(oct(i)[2:]).rjust(width, ' '), str(hex(i)[2:]).upper().rjust(width, ' '),
              str(bin(i)[2:]).rjust(width, ' '))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Sample Input

# 17
