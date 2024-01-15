# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
# Returns: string: a single string with newline characters ('\n') where the breaks should be

import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    wordList = wrapper.fill(text=string)

    return wordList


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Sample Input

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
