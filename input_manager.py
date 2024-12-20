'''
FILNAMN.PY: Interaktiv produktlager gjort med biblioteket ”Curses”.

__author__  = "Daniil Gurski"
__version__ = "1.0.0"
__email__   = "daniil.gurski@elev.ga.ntig.se"
'''

import curses

class InputManager():
    def __init__(self, stdscr): 
        self.stdscr = stdscr
    

    # simulate input() function in curses
    def get_input(self, prompt: str):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, prompt)
        self.stdscr.refresh()
        curses.echo()
        input_str = self.stdscr.getstr(1, 0).decode('utf-8')
        curses.noecho()
        return input_str

    
    def get_product_input(self, prefix: str):
        name = self.get_input(f"{prefix} name: ")
        desc = self.get_input(f"{prefix} description: ")

        while True:
            price = self.get_input(f"{prefix} price: ")

            try:
                price = float(price)
                break
            except ValueError:
                continue
        

        while True:
            quantity = self.get_input(f"{prefix} quantity: ")
            try:
                quantity = int(quantity)
                break
            except ValueError:
                continue
            
        return (name, desc, price, quantity)