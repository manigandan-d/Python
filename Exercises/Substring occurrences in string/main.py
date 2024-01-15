# In this challenge, the user enters a string and a substring. You have to print the number of times that the
# substring occurs in the given string.

def count_substring(string, sub_string):
    cnt = 0
    startInd = 0

    for i in range(len(string)):
        ind = string.find(sub_string, startInd)

        if ind != -1:
            startInd = ind + 1
            cnt += 1

    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# ABCDCDC
# CDC
