inventory = {'Arrow': 13, 'Gold': 10023 , 'Sword' : 10, 'Beer': 1 , 'Coat': 3}
loot = ['Gold', 'Gold', 'Sword', 'Dagger', 'Ruby', 'Glass' ]

def looting():
    for i in loot:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 0)
            inventory[i] = inventory[i] + 1
    return inventory

def displayInv(inv):
    print('Inventory')
    items_total_start = 0
    for a , b in inv.items():
        print(str(b) + ' ' + a)
        items_total_start += b
    print('Total ' + str(items_total_start))

displayInv(looting())
