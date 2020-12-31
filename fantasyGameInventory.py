from gameInventory import displayInventory
def addToInventory(inventory, addedItems):
    for items in addedItems:
        out = inventory.setdefault(items, 0)
        if out!=0:
            inventory[items]+=1
        else:
            inventory[items]=1
    displayInventory(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

