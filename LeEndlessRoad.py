from Functions import check_supplies, hunt

game_over = False
inventory = {
    'food': 10,
    'bottles of water': 10,
    'arrows': 5,
    'gold coins': 3
}
print('intro')
while not game_over:
    print('\n\nchoices:\n0.Quit game\n1.Hunt\n2.Enter shop\n3.Check supplies')
    choice = input('What should we do?\n')
    if choice == '3':
        check_supplies(inventory)
    elif choice == '1':
        if inventory['arrows'] == 0:
            print('out of arrows')
        else:
            inventory = hunt(inventory)
            check_supplies(inventory)
    elif choice == '0':
        print('good bye')
        break
    elif choice == '2':
        shop = {
            '0.Leave shop': 0,
            '1.Food selling price': 1,
            '2.Bottles of water price': 1,
            '3.arrows price': 2
        }
        while True:
            check_supplies(shop)
            choice2 = input('\nWhat do you want to buy?\n')
            if choice2 == '3':
                inventory['gold coins'] -= shop['3.arrows price']
                inventory['arrows'] += 1
            elif choice2 == '1':
                inventory['gold coins'] -= shop['1.Food selling price']
                inventory['food'] += 1
            elif choice2 == '0':
                print('do come again')
                break
            elif choice2 == '2':
                inventory['gold coins'] -= shop['2.Bottles of water price']
                inventory['bottles of water'] += 1
            check_supplies(inventory)