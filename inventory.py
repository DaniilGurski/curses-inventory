'''
FILNAMN.PY: Interaktiv produktlager gjort med biblioteket ”Curses”.

__author__  = "Daniil Gurski"
__version__ = "1.0.0"
__email__   = "daniil.gurski@elev.ga.ntig.se"
'''


from csv import DictReader, DictWriter
from product import Product
import os


class Inventory(): 
    def __init__(self, products=None, source_file=str) -> None: 
        if products is None:
            products = []
        self.products = products
        self.source_file = source_file


    def get_product(self, id): 
        for product in self.products: 
            if product.id == int(id):
                return product
        return None


    def delete_product(self, index): 
        self.products.pop(index)


    def add_product(self, name, desc, price, quantity):
        new_id = self.create_unquie_id()
        self.products.append(Product(new_id, name, desc, price, quantity))

        return self.products


    def edit_product(self, index, name, desc, price, quantity): 
        product_to_edit = self.products[index]
        
        # if the user didn't enter a value, keep the old one
        product_to_edit.name = name if name != "" else product_to_edit.name
        product_to_edit.desc = desc if desc != "" else product_to_edit.desc
        product_to_edit.price = price  if price != "" else product_to_edit.price
        product_to_edit.quantity = quantity if quantity != "" else product_to_edit.quantity

        return self.products


    def create_unquie_id(self) -> int : 
        unquie_id = max([product.id for product in self.products]) + 1
        return unquie_id
    

    def save_to_inventory(self):
        try:
            with open(self.source_file, mode="w") as csvfile:
                fieldnames = ["id", "name", "desc", "price", "quantity"]
                writer = DictWriter(csvfile, fieldnames)

                writer.writeheader()
                for product in self.products:
                    writer.writerow({
                        "id": product.id,
                        "name": product.name,
                        "desc": product.desc,
                        "price": product.price,
                        "quantity": product.quantity
                    })

                return "Done !"
            
        except Exception as error_code:

            # in case file is read-only or corrupt 
            if isinstance(error_code, OSError) and error_code.errno == 13:
                print("Cause: File is read-only")
            else:
                print(f"Cause: {error_code}")
                
            return "Error"


    @staticmethod
    def load_inventory(filename): 
        products = []
        
        # Check if the file exists
        if not os.path.exists(filename):
            # Create the file and write the header row
            with open(filename, 'w', newline='') as file:
                writer = DictWriter(file, fieldnames=["id", "name", "desc", "price", "quantity"])
                writer.writeheader()

            return products
    
        with open(filename, 'r') as file:
            reader = DictReader(file)

            for row in reader:
                id       = int(row['id'])
                name     = row['name']
                desc     = row['desc']
                price    = row['price']
                quantity = row['quantity']
                
                products.append(Product(id, name, desc, price, quantity))

        return products



