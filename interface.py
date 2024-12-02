import curses

class Interface:
    def __init__(self, stdsrc, products) -> None: 
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        self.stdsrc = stdsrc
        self.products = products
        self.width, self.height = self.stdsrc.getmaxyx()


    def add_string(self, string, color_id=curses.COLOR_WHITE):
        self.stdsrc.addstr(f"{string}\n", curses.color_pair(color_id))

    
    def product_details(self, product_position): 
        selected_product = self.products[product_position]
        self.add_string(f"Name: {selected_product.name}")
        self.add_string(f"Description: {selected_product.desc}")
        self.add_string(f"Price: {selected_product.price}")
        self.add_string(f"Quantity: {selected_product.quantity}")

        self.add_string(f"\nHandle this product", 3)

        self.add_string(f"\nSPACE: Edit")
        self.add_string(f"D: Delete")
        self.add_string(f"ENTER: Go back")

    
    def menu_details(self):
        self.add_string(f"{'Dan4ik':<41} ↑ ↓ = Navigate | ENTER = Select | N = New product | Q = Exit", 1)
        self.add_string("---" * 35)

        self.add_string(f"{'#'} {'NAME':>7} {'DESC':>26} {'PRICE':>53} {'QUANTITY':>17}")


    def show_screen(self, name, product_position=None):
        if name == "menu":
            self.menu_details()
        elif name == "product": 
            try:
                self.product_details(product_position)
            except: 
                return "No id provided"


    def display_products(self, selected): 
        if not len(self.products):
            self.add_string("No products found.")
        
        for index, product in enumerate(self.products): 
            if index == selected: 
                self.add_string(f"{product}", 2)
            else:
                self.add_string(f"{product}")


    def update_products(self, new_products):
        self.products = new_products

