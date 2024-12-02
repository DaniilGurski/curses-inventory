class Product:
    def __init__(self, id: str, name: str, desc: str, price: str, quantity: str) -> None:
        self.character_limits = {
            "name": 23,
            "desc": 48, 
        }

        self.id = id
        self.name = name
        self.desc = desc
        self.price = f"{price} kr"
        self.quantity = quantity


    def limit_characters(self, string: str, data: str) -> str: 
        if len(string) > self.character_limits[data]:
            return f"{string[:self.character_limits[data]]}..."
        
        return string
        

    def __str__(self) -> str:  
        self.name_lim = self.limit_characters(self.name, "name")    # I use self.name instead of name in case to sync changes.
        self.desc_lim = self.limit_characters(self.desc, "desc")   
        
        return f"{self.id:<4} {self.name_lim:<26} {self.desc_lim}  {self.price:<15}  {self.quantity}"
        