from abc import ABCMeta, abstractmethod
from enum import Enum

class VehicleType(Enum):
    BIKE = 0
    CAR = 1
    TRUCK = 2

class SpotSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

class Vehicle(metaclass = ABCMeta):
    
    def __init__(self, registration: str , vehicleType: VehicleType , entry_time : str):
        self.registration = registration
        self.type = vehicleType
        self.entry_time = entry_time
        self.exit_time = None
        self.assigned_spot = None
    
    def set_assigned_spot(self , spot: Spot):
        self.assigned_spot = spot
    
    def vacate(self):
        self.assigned_spot = None
    
    @abstractmethod
    def can_fit(self, spot):
        pass

class Bike(Vehicle):
    
    def __init__(self ,registration: str , entry_time : str ):
        super().__init__(registration , VehicleType.BIKE , entry_time)
    
    def can_fit(self , spot: Spot):
        return spot.size == SpotSize.LARGE or spot.size == SpotSize.MEDIUM or spot.size == SpotSize.SMALL

class Car(Vehicle):
    
    def __init__(self ,registration: str , entry_time : str ):
        super().__init__(registration , VehicleType.CAR , entry_time)
    
    def can_fit(self , spot: Spot):
        return spot.size == SpotSize.LARGE or spot.size == SpotSize.MEDIUM

class Truck(Vehicle):
    
    def __init__(self ,registration: str , entry_time : str ):
        super().__init__(registration , VehicleType.TRUCK , entry_time)
    
    def can_fit(self , spot : Spot):
        return spot.size == SpotSize.LARGE
    


class Spot(object):
    
    def __init__(self ,id , size : SpotSize):
        self.id = id
        self.size = size
        self.available = True
        self.vehicle = None
        
    def park(self, vehicle: Vehicle):
        if self.available and vehicle.can_fit(self):
            self.vehicle = vehicle
            self.available = False
            vehicle.set_assigned_spot(self)
    
    def vacate_spot(self , vehicle : Vehicle):
        self.available = True
        self.vehicle = None
        vehicle.vacate()


class Level(object):
    def __init__(self,floor):
        self.floor = floor
        self.spots = []
    
    def add_spot(self , spot: Spot):
        self.spots.append(spot)
    
    def _accomodate(self, vehicle: Vehicle):
        pass
    
    def spot_finder(self, vehicle: Vehicle):
        spot = self._accomodate(vehicle)
        return spot
    
    
class ParkingLot(object):
    def __init__(self):
        self.levels = []
        self.billingService = BillingService() 
    def add_level(self , level : Level):
        self.levels.append(level)
    
    def park_vehicle(self,registration: str , size : VehicleType):
        # create vehicle based on type
        vehicle = Bike(registration=registration , vehicleType= size, entry_time=curr.time)
        if self._findSpot(vehicle):
            print("vehicle Parked")
        else:
            print("parking lot full")
    
    def _findSpot(self , vehicle : Vehicle):
        for level in self.levels:
            spot = level.spot_finder(vehicle)
            if spot:
                spot.park(vehicle)
                return True
        return False
    
    def exit_vehicle(self , vehicle : Vehicle):
        vehicle.exit_time = curr.time
        self.billingService.generate_bill(vehicle)
        if vehicle.assigned_spot:  # Ensure the vehicle has a spot before vacating
            vehicle.assigned_spot.vacate_spot()      
        
class BillingService(object):
    def __init__(self):
        pass
    
    def generate_bill(self , vehicle: Vehicle):
        pass