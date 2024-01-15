# find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase
# characters.

if __name__ == '__main__':
    s = input()

    for i in s:
        if i.isalnum():
            print(True)
            break

    else:
        print(False)

    for i in s:
        if i.isalpha():
            print(True)
            break

    else:
        print(False)

    for i in s:
        if i.isdigit():
            print(True)
            break

    else:
        print(False)

    for i in s:
        if i.islower():
            print(True)
            break

    else:
        print(False)

    for i in s:
        if i.isupper():
            print(True)
            break

    else:
        print(False)

# Sample Input

# qA2
