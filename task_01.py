from abc import ABC, abstractmethod
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Abstract base class Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

# Car class inheriting from Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(Fore.GREEN + f"{self.make} {self.model} ({self.spec}): " + Style.RESET_ALL + Fore.YELLOW + "Engine started" + Style.RESET_ALL)

# Motorcycle class inheriting from Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        print(Fore.BLUE + f"{self.make} {self.model} ({self.spec}): " + Style.RESET_ALL + Fore.YELLOW + "Engine started" + Style.RESET_ALL)


# Abstract class VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Factory implementation for the US
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")

# Factory implementation for the EU
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")

# Example usage
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Creating vehicles for the US
us_car = us_factory.create_car("Ford", "Mustang")
us_motorcycle = us_factory.create_motorcycle("Indian", "Scout")

# Creating vehicles for the EU
eu_car = eu_factory.create_car("BMW", "3 Series")
eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")

# Starting engines
us_car.start_engine()
us_motorcycle.start_engine()
eu_car.start_engine()
eu_motorcycle.start_engine()

# Additional example usage
# Creating more vehicles for demonstration
another_us_car = us_factory.create_car("Tesla", "Model S")
another_eu_motorcycle = eu_factory.create_motorcycle("KTM", "Duke 390")

# Starting engines for the additional vehicles
another_us_car.start_engine()
another_eu_motorcycle.start_engine()
