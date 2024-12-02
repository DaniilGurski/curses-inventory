from csv import DictReader, DictWriter
from product import Product


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
        # removed_product = self.get_product(id)
        self.products.pop(index)


    def add_product(self, name, desc, price, quantity):
        new_id = self.create_unquie_id()
        self.products.append(Product(new_id, name, desc, price, quantity))

        return self.products


    def edit_product(self, index, name, desc, price, quantity): 
        product_to_edit = self.products[index]
        
        product_to_edit.name = name
        product_to_edit.desc = desc
        product_to_edit.price = price
        product_to_edit.quantity = quantity

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
    
        with open(filename, 'r') as file:
            reader = DictReader(file)

            for row in reader:
                # TODO: add type convertations
                id       = int(row['id'])
                name     = row['name']
                desc     = row['desc']
                price    = row['price']
                quantity = row['quantity']
                
                products.append(Product(id, name, desc, price, quantity))

        return products



