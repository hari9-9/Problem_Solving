from enum import Enum
from abc import ABC, abstractmethod
class RoomType(Enum):
    SINGLE = "single"
    DOUBLE = "double"
    DELUXE = "deluxe"


class Room(object):
    def __init__(self , room_number: int , room_type : RoomType , price : float):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self._is_available = True
        self.guest = None
        
    def room_available(self) -> bool:
        return self._is_available
    
    def book_room(self , guest : Guest):
        if self.room_available():
            self._is_available = False
            self.guest = guest
        else:
            raise Exception("Room is already booked")
    
    def checkout_room(self):
        self.guest = None
        self._is_available = True
        

class Guest(object):
    
    def __init__(self , guest_id : int , name : str , contact : str):
        self.guest_id = guest_id
        self.name = name
        self.contact = contact


class Reservation(object):
    def __init__(self , guest : Guest , room : Room , checkin_date : str , checkout_date : str):
        self.guest = guest
        self.room = room
        self.chekin_date = checkin_date
        self.checkout_date = checkout_date
        self.is_checked_in = False
    
    def check_in(self):
        if self.room.room_available():
            self.room.book_room(self)
            self.is_checked_in = True
        else:
            raise Exception("Room has been booked")
    
    def check_out(self):
        self.room.checkout_room()


class PaymentMethod(ABC):
    
    @abstractmethod
    def process_payment(self , amount: float):
        pass


class cashPayment(PaymentMethod):
    def process_payment(self, amount):
        pass

class OnlinePayment(PaymentMethod):
    def process_payment(self, amount):
        pass



class Hotel(object):
    def __init__(self , name : str):
        self.name = name
        self.rooms = {}
        self.guests = {}
        self.reservations = []
    
    def add_room(self , room_number : int , room_type : RoomType , price : float ):
        if room_number in self.rooms:
            raise Exception("Room already exists") 
        self.rooms[room_number] = Room(room_number, room_type,price)
    
    def add_guest(self , guest_id: int , name : str , contact : str):
        if guest_id in self.guests:
            raise Exception("duplicate guest cant be created")
        self.guests[guest_id] = Guest(guest_id , name , contact)
    
    
    def _find_room(self, room_type : RoomType) -> Room:
        # find room of room type that is available
        pass
    
    def make_reservation(self , guest_id: int , room_type : RoomType , chekin_date: str , checkout_date: str):
        if guest_id not in self.guests:
            raise Exception("Guest does not exist")
        room = self._find_room(room_type)
        if not room:
            raise Exception("All rooms full")
        guest = self.guests[guest_id]
        reservation = Reservation(guest , room , chekin_date,  checkout_date)
        self.reservations.append(reservation)
    
    def process_payment(self, amount: float, method: str):
        payment_processor: PaymentMethod
        if method == "CASH":
            payment_processor = cashPayment()
        elif method == "ONLINE":
            payment_processor = OnlinePayment()
        else:
            raise Exception("Invalid payment method")
        payment_processor.process_payment(amount)