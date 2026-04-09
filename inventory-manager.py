

inventory = []

#function to add item to inventory
def add_item(item , quantity):
   
    stock = {
        'name' : item,
        'quantity' : quantity
    }
    inventory.append(stock)
    print(f'{quantity} {item}(s) have been added to the inventory.')
    


#function to remove item from inventory
def remove_item(item):
    for stock in inventory:
        if stock['name'].lower() == item.lower():
            inventory.remove(stock)
            print(f'{item} has been removed from the inventory.')
            break
    else:
        print(f'{item} is not in the inventory.')



while True:         
    print('=== Inventory Manager ===')
    print('1. View all items')
    print('2. Add an item')
    print('3. Remove an item')
    print('4. Quit')
    
    choice = input('Choose an option: ')
    if choice not in ['1', '2', '3', '4']:
        print('invalid option')
        exit()
    
    if choice == '1':
        #print('these are all items')
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item['name']} - {item['quantity']}")
            #print[(items) for items in item]
    
        if len(inventory) == 0:
            print('No items in inventory')
            
    elif choice == '2':
        item = input('Enter the name of the item to add: ')
        quantity = int(input('specify the quantity: '))
        
        add_item(item , quantity)

    elif choice == '3':
        item = input('Enter the name of the item to remove: ')
        remove_item(item)

    elif choice == '4':
        print('Thanks for choosing our product!')
        print('Goodbye!')
        break
   
    

