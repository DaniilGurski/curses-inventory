class Product:
    def __init__(self, id: str, name: str, desc: str, price: str, quantity: str) -> None:
        self.character_limits = {
            "name": 23,
            "desc": 48, 
        }

        self.id = id
        self.name = self.limit_characters(name, "name")
        self.desc = self.limit_characters(desc, "desc")
        self.price = f"{price} kr"
        self.quantity = quantity


    def limit_characters(self, string: str, data: str) -> str: 
        if len(string) > self.character_limits[data]:
            return f"{string[:self.character_limits[data]]}..."
        
        return string
        

    def __str__(self) -> str:     
        return f"{self.id:<4} {self.name:<26} {self.desc}  {self.price:<15}  {self.quantity}"
        