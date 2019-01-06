inventory = {'Arrow': 13, 'Gold': 10023 , 'Sword' : 10, 'Beer': 1 , 'Coat': 3}

def displayInv(inv):
    print('Inventory')
    items_total_start = 0
    for a , b in inv.items():
        print(str(b) + ' ' + a)
        items_total_start += b
    print('Total ' + str(items_total_start))
displayInv(inventory)

Loot = ['Gold', 'Dagger', 'Gold', 'Sword']
