from csv import DictReader
from product import Product


class Inventory(): 
    def __init__(self, products=None, source_file=str) -> None: 
        if products is None:
            products = []
        self.products = products
        self.source_file = source_file


    def get_product(self, id): 
        pass


    def remove_product(self, id): 
        pass


    def add_product(self, name, desc, price, quantity):
        pass


    def edit_product(self, id, name, desc, price, quantity): 
        pass


    def create_unquie_id(self): 
        pass


    @staticmethod
    def load_inventory(filename): 
        products = []
    
        with open(filename, 'r') as file:
            reader = DictReader(file)

            for row in reader:
                # TODO: add type convertations
                id       = row['id']
                name     = row['name']
                desc     = row['desc']
                price    = row['price']
                quantity = row['quantity']
                
                products.append(Product(id, name, desc, price, quantity))

        return products



