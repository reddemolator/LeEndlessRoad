def check_supplies(inventory):
    for key, value in inventory.items():
        print(key, value)


def hunt(inventory):
    inventory['arrows'] -= 1
    inventory['food'] += 6
    return inventory
