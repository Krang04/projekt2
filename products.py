"""Functions for buying products in the store"""

#The products available in the store
products = {'apples': {'price': 0.50, 'quantity': 100},
            'bananas': {'price': 0.25, 'quantity': 50},
            'oranges': {'price': 0.75, 'quantity': 75}}

def display_products(product):
    """Display the products, how much they cost and how many are in stock"""
    print('Products:')
    for item in product:
        print(item, '- Price:', product[item]['price'], '- Quantity:', product[item]['quantity'])

def process_order(products_1):
    """Buying products and printing the receipt"""
    order_total = 0
    order_items = {}
    funds = float(input('Enter available funds: '))

    while True:
        item = input('Enter item name (press Enter to complete order): ')
        if not item:
            break

        if item not in products_1:
            print('Sorry, item not found among products.')
            continue

        quantity = int(input('Enter quantity: '))
        if quantity > products_1[item]['quantity']:
            print('Sorry, item is out of stock.')
            continue

        #Check if the customer has enough funds for the wanted amount of items
        item_cost = products_1[item]['price'] * quantity
        if item_cost > funds:
            print('Sorry, you cannot afford that item.')
            continue

        order_items[item] = quantity
        products_1[item]['quantity'] -= quantity
        order_total += item_cost
        funds -= item_cost

    #Prints a receipt with the items bought and the total costs
    print('Receipt:')
    for item in order_items:
        print(item, '- Quantity:', order_items[item],'- Price:', products_1[item]['price'],
            '- Total:', products_1[item]['price'] * order_items[item])

    print('Order total:', order_total)
    print('Remaining funds:', funds)
