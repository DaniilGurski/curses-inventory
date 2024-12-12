'''
FILNAMN.PY: Interaktiv produktlager gjort med biblioteket ”Curses”.

__author__  = "Daniil Gurski"
__version__ = "1.0.0"
__email__   = "daniil.gurski@elev.ga.ntig.se"
'''

class Product:
    def __init__(self, id: str, name: str, desc: str, price: str, quantity: str) -> None:
        self.character_limits = {
            "name": 23,
            "desc": 48, 
            "price": 8,
        }

        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity


    def truncate(self, string: str, data: str) -> str: 
        if len(string) > self.character_limits[data]:
            return f"{string[:self.character_limits[data]]}..."
        
        return string
        

    def __str__(self) -> str:  
        self.name_lim = self.truncate(self.name, "name")    # I use self.name instead of name in case to sync changes.
        self.desc_lim = self.truncate(self.desc, "desc")   
        self.price_lim = self.truncate(str(self.price), "price")
        
        return f"{self.id:<4} {self.name_lim:<26} {self.desc_lim:<53}  {f'{self.price_lim} kr':<15} {self.quantity}"
        