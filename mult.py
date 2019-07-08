def input_list():
    line = input()
    values = list(map(int, line.split()))
    return values


def sum_lists(l1, l2):
    l3 = []
    minimum = min(len(l1), len(l2))
    for n in range(0, minimum):
        l3.append(l1[n] + l2[n])
    if len(l1) > minimum:
        for n in range(minimum, len(l1)):
            l3.append(l1[n])

    if len(l2) > minimum:
        for n in range(minimum, len(l2)):
            l3.append(l2[n])

    return l3


def mul(x, l):
    multiplied = []
    for i in l:
        multiplied.append(x * i)
    return multiplied


def print_all(l):
    for i in l:
        print(i)


if __name__ == "__main__":
    A = input_list()
    B = input_list()
    C = sum_lists(A, B)
    x = 10;
    D = mul(x, C)
    print_all(D)