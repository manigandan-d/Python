import textwrap

data = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

# wrapper = textwrap.TextWrapper(width=max_width)
# wordList = wrapper.wrap(text=data)
#
# for i in wordList:
#     print(i)

wordList = textwrap.wrap(data, max_width)
for i in wordList:
    print(i)

string = textwrap.fill(data, max_width)
print(string)
