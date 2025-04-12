# have a menu of dishes
# ability to mark a dish as available or unavailable
# ability to add a dish to the menu
# ability to remove a dish from the menu
# receptionist to help find table
# receptionist to help bill the table
# waiters to be assigned to multiple tables max 3
# waiter to add a dish to order
# chef to take up order in sequence and mark them ready

# enum dish as availble or unavailable
# class Dish to hold name and availblility enum
# class Menu to hold all dishes
# class Order to take dish id and table number and waiter to call
# class Table to hold table number and waiter assigned and dishes ordered
# class chef to pick up orders and complete them and also set menu items as avialble or not
# class chef to add itms to menu

from enum import Enum

class DishAvailability(Enum):
    AVAILABLE = 1
    UNAVAILABLE = 0

class Dish(object):
    def __init__(self ,id: int, name: str ,availablity: DishAvailability ):
        self.id = id
        self.name = name
        self.availability = availablity

class Menu(object):
    def __init__(self):
        self.dishes = {} # id:Dish
    
    def add_dish(self , dish : Dish):
        self.dishes[dish.id] = dish
    
    def remove_dish(self , id : int):
        if id in self.dishes:
            del self.dishes[id]

class Customer(object):
    def __init__(self , id, name , table: Table):
        self.id = id
        self.name = name
        self.table = table


class Table(object):
    def __init__(self , id):
        self.id = id
        self.customer = None
        self.available = True
        self.waiter = None
        self.orders = []
    
    def add_customer(self , customer: Customer):
        self.customer = customer
        self.available = False
    
    


        