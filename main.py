import curses
from curses import wrapper 
from inventory import Inventory
from interface import Interface
from input_manager import InputManager

def main(stdscr): 
    stdscr.clear()
    stdscr.keypad(True)

    products_path = "products.csv"
    items = Inventory.load_inventory(products_path)
    inventory = Inventory(items, products_path)
    interface = Interface(stdscr, inventory.products)
    input_manager = InputManager(stdscr)
    
    selected_product_index = 0
    current_screen = "menu"

    while True: 
        stdscr.clear()

        if interface.is_window_small():
            interface.add_string("Window too small. Please resize !", 3)
            stdscr.refresh()
            stdscr.getch()
            continue

        interface.show_screen(current_screen, selected_product_index)

        if current_screen == "menu":
            interface.display_products(selected_product_index)
            stdscr.refresh()
            key = stdscr.getkey()

            if key == "KEY_C2": 
                selected_product_index += 1

                if selected_product_index >= len(inventory.products):
                    selected_product_index = 0

            elif key == "KEY_A2": 
                selected_product_index -= 1

                if selected_product_index < 0:
                    selected_product_index = len(inventory.products) - 1

            elif key == "n":
                current_screen = "new product"

            elif key == '\n' or key == '\r': 
                current_screen = "product"

            elif key == "q": 
                break

        elif current_screen == "product":
            stdscr.refresh()
            key = stdscr.getkey()

            if key == '\n' or key == '\r': 
                current_screen = "menu"
            
            elif key == "d":
                inventory.delete_product(selected_product_index)
                selected_product_index = len(inventory.products) - 1
                current_screen = "menu"

            elif key == " ":
                current_screen = "edit"

        elif current_screen == "new product":
            name, desc, price, quantity = input_manager.get_product_input("Enter new product")
            updated_product_list = inventory.add_product(name, desc, price, quantity)
            interface.update_products(updated_product_list)
            current_screen = "menu"

        elif current_screen == "edit":
            name, desc, price, quantity = input_manager.get_product_input("Enter updated product")

            edited_product_list = inventory.edit_product(selected_product_index, name, desc, price, quantity)
            interface.update_products(edited_product_list)
            current_screen = "menu"
    
        inventory.save_to_inventory()


wrapper(main)