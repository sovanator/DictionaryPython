def displayInventory(stuffParm):
    total =0
    print('Inventory:')
    for k,v in stuff.items():
        print(str(v)+' '+ str(k))
        total+=v
    print('Total number of items:', total)
displayInventory(stuff)