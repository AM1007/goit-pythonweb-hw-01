from abc import ABC, abstractmethod
from colorama import Fore, Style, init
import logging
from typing import Type

# Initialize colorama
init(autoreset=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make: str = make
        self.model: str = model
        self.spec: str = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f"{Fore.GREEN}{self.make} {self.model} ({self.spec}): {Style.RESET_ALL}{Fore.YELLOW}Engine started{Style.RESET_ALL}"
        )


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(
            f"{Fore.BLUE}{self.make} {self.model} ({self.spec}): {Style.RESET_ALL}{Fore.YELLOW}Engine started{Style.RESET_ALL}"
        )


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Example usage
def main() -> None:
    us_factory: Type[VehicleFactory] = USVehicleFactory()
    eu_factory: Type[VehicleFactory] = EUVehicleFactory()

    # Creating vehicles for the US
    us_car: Car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle: Motorcycle = us_factory.create_motorcycle("Indian", "Scout")

    # Creating vehicles for the EU
    eu_car: Car = eu_factory.create_car("BMW", "3 Series")
    eu_motorcycle: Motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")

    # Starting engines
    us_car.start_engine()
    us_motorcycle.start_engine()
    eu_car.start_engine()
    eu_motorcycle.start_engine()

    # Additional example usage
    another_us_car: Car = us_factory.create_car("Tesla", "Model S")
    another_eu_motorcycle: Motorcycle = eu_factory.create_motorcycle("KTM", "Duke 390")

    # Starting engines for the additional vehicles
    another_us_car.start_engine()
    another_eu_motorcycle.start_engine()


if __name__ == "__main__":
    main()