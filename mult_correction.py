def input_arr(size):
    my_list = []
    for i in range(size):
        x = int(input())
        my_list.append(x)
    return my_list


def add (a,b):
    for i in range(len(a)):
        a[i] = a[i] + b[i]
    return a


print("enter your first list:")
A = input_arr(3)
print("enter your second list:")
B = input_arr(3)
C = add (A,B)

print (C)


x = 10
def mul (x,C):
    list_d = []
    for i in C:
        list_d.append (x*i)
    return list_d
print (mul(x,C))