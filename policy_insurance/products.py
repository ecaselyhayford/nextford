
class Products():
    def __init__(self, product_id=None, name=None, price=None):  # constructor
        self.active = True
        self.name = name
        self.product_id = product_id
        self.price = price

    def create_product(self):  # create a new product
        print(
            f"Product {self.name} created with ID {self.product_id} and price ${self.price}.")

    def update_product(self, name, price):  # update product details
        self.name = name
        self.price = price
        print(f"Product {self.name} and price {self.price} updated.")

    def suspend_product(self):  # suspend a product
        if not self.active:
            print(f"Product {self.name} is already suspended.")
            return
        self.active = False
        print(f"Product {self.name} suspended.")
