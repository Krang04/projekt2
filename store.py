"""Main file to run the program in"""

from products import products, display_products, process_order



def main():
    """Function for running the program"""
    while True:
        display_products(products)
        choice = input('Would you like to place an order? (y/n): ')
        if choice.lower() == 'n':
            break
        process_order(products)

if __name__ == '__main__':
    main()
