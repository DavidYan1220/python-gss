player = {}
menu = ''

for i in range(1, 6):
    number = int(input('Enter player %d\'s jersey number: ' % i))
    rating = int(input('Enter player %d\'s rating: ' % i))
    player[number] = rating

list_of_number = sorted(list(player.keys()))

print('ROSTER')
for i in list_of_number:
    print('Jersey number: %d, Rating: %d' % (i, player[i]))

while menu != 'q':
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')

    menu = input('Choose an option: ')

    if menu == 'a':
        number = int(input('Enter a new player\'s jersey number: '))
        rating = int(input('Enter the player\'s rating: '))
        player[number] = rating

    elif menu == 'd':
        number = int(input('Enter a jersey number: '))
        del player[number]

    elif menu == 'u':
        number = int(input('Enter a jersey number: '))
        rating = int(input('Enter a new rating for player: '))
        player[number] = rating

    elif menu == 'r':
        rating = int(input('Enter a rating: '))
        list_of_number = sorted(list(player.keys()))

        print('Above', rating)
        for i in list_of_number:
            if player[i] > rating:
                print('Jersey number: %d, Rating: %d' % (i, player[i]))

    elif menu == 'o':
        list_of_number = sorted(list(player.keys()))
        print('ROSTER')
        for i in list_of_number:
            print('Jersey number: %d, Rating: %d' % (i, player[i]))

