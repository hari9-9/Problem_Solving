# should support multiple products with different prices and quantities.
# should accept coins and notes of different denominations.
# should dispense the selected product and return change if necessary.
# should keep track of the available products and their quantities.
# should handle multiple transactions concurrently and ensure data consistency.
# should provide an interface for restocking products and collecting money.
# should handle exceptional scenarios, such as insufficient funds or out-of-stock products.

from threading import Lock

class Product(object):
    def __init__(self , name : str ,  price: int , quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def is_available(self) -> bool:
        return self.quantity > 0
    
    def reduce_quantity(self , count : int = 1):
        if self.quantity >= count:
            self.quantity -= count
        else:
            raise ValueError("not enough stock to vend")
    
    def restock(self , count : int):
        self.quantity +=count
        return
    

class Payment(object):
    
    @staticmethod
    def validate_payment(inserted_amount : int , product_price: int) -> bool :
        return inserted_amount >= product_price
    
    @staticmethod
    def calculate_change(inserted_amount : int , product_price: int):
        #calculates optimal change
        pass


class VendingMachine(object):
    
    def __init__(self):
        self.products: Dict[int , Product] = {}
        self.balance = 0
        self.lock = Lock()
    
    
    def add_products(self , product_id : int , product : Product):
        self.products[product_id] = product
    
    def display_products(self):
        for pid , product in self.products.items():
            print(f"ID: {pid}, Name: {product.name}, Price: {product.price / 100:.2f}$, Stock: {product.quantity}")
    
    def purchase_product(self , inserted_amount : int , product_id : int):
        with self.lock:
            if product_id not in self.products:
                raise ValueError("Invalid product selected")
            
            product = self.products[product_id]
            
            if not product.is_available():
                raise ValueError("Product not in stock")
            
            if not Payment.validate_payment(inserted_amount , product.price):
                raise ValueError("Payment Failure")
            
            self.balance +=product.price
            
            try:
            
                change = Payment.calculate_change(inserted_amount, product.price)
                self.balance -=change
                product.reduce_quantity()
            except:
                self.balance -=product.price
                raise ValueError("transaction failed")
            
            return change
        
    def restock_product(self, product_id: int, quantity: int):
        """Restocks a product."""
        if product_id not in self.products:
            raise ValueError("Invalid product ID.")
        
        self.products[product_id].quantity += quantity
    
    def collect_money(self):
        """Allows an administrator to collect money from the machine."""
        collected_amount = self.balance
        self.balance = 0  # Reset balance after collection
        print(f"Collected {collected_amount / 100:.2f}$ from the vending machine.")
