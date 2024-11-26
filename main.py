import curses
from curses import wrapper 
from inventory import Inventory
from interface import Interface


def main(stdsrc): 
    stdsrc.clear()

    products_path = "products.csv"
    items = Inventory.load_inventory(products_path)
    inventory = Inventory(items, products_path)
    interface = Interface(stdsrc)
    
    while True: 
        interface.display_products(inventory.products)
        stdsrc.refresh()
        key = stdsrc.getkey()


wrapper(main)