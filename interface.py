class Interface:
    def __init__(self, stdsrc) -> None: 
        self.stdsrc = stdsrc


    def add_string(self, string): 
        self.stdsrc.addstr(string + "\n")

    
    def edit_details(self): 
        pass

    
    def menu_details(self):
        pass


    def display_products(self, products): 
        if not len(products):
            self.add_string("No products found.")
        
        for index, product in enumerate(products): 
            self.add_string(f"{product}")
