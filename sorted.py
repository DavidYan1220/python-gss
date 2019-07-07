I = [6, 32, 94, 76, 25, 73]
for m in range(0, len(I)-1):
    for n in range(m+1, len(I)):
        if I[m] > I[n]:
            temp = I[n]
            I[n] = I[m]
            I[m] = temp
print(I)


