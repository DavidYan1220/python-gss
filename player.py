def input_p():
    player = {}
    list = []
    for i in range(5):
        number = int(input("Enter player's number:"))
        rating = int(input("Enter player's rating:"))
        player[number] = rating
    for x in player:
        list.append(x)
    list.sort()
    for b in list:
        print("player number is %d and the rating is %d" % (b, player[b]))

a = input_p()
print(a)


