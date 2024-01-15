# perform the modification in string which is immutable

def mutate_string(string, position, character):
    data = list(string)

    data[position] = character

    return "".join(data)


if __name__ == '__main__':
    s = input()
    i, c = input().split()

    s_new = mutate_string(s, int(i), c)

    print(s_new)

# abracadabra
# 5 k
