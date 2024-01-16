# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
# Returns: string: a single string with newline characters ('\n') where the breaks should be

import textwrap


def wrap(s, mw):
    res = textwrap.fill(s, mw)

    return res


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Sample Input

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
