x = int(input("Enter a number :"))
number = [3, 7, 8, 9, 12]


def my_search(f):
    if f in number:
        index = number.index(x)
        print('Element %d: %s' % (index, x))
    else:
        print("Item mot found")
    return


my_search(x)





