lst = ['David Yan', 'Claire Lu', 'Leo Xu', 'Bob Pan', 'Nina Ai']
names = sorted(lst)
print(names)
n = len(names) - 1


low = 0
high = n
key = input("Please enter a name:")


def binary_search(a, l, h, k):

    if h < l:
        return l - 1
    mid = l + (h - l // 2)
    if k == names[mid]:
        return mid
    elif key < names[mid]:
        return binary_search(a, l, mid-1, k)
    else:
        return binary_search(a, mid+1, h, k)


index = binary_search(names, low, high, key)
print("The given name ", key, "is at place ", index)