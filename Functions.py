def check_supplies(inventory):
    for key, value in inventory.items():
        print(key, value)


def hunt(inventory, game_over):
    if inventory['bottles of water'] == 0 or inventory['food'] == 0:
        game_over = True
    else:
        inventory['food'] -= 1
        inventory['bottles of water'] -= 1
        inventory['arrows'] -= 1
        inventory['food'] += 3
    return inventory, game_over
