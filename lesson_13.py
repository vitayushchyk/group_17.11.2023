from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(
            self,
            brand: str, fuel_in_tank: float,
            speed: float, mileage: float,
            tank_volume: float = 80
    ):
        self.brand = brand
        self.tank_volume = tank_volume
        self.fuel_in_tank = fuel_in_tank
        self.speed = speed
        self.mileage = mileage

    def fuel_add(self, volume: float):
        if self.fuel_in_tank + volume > self.tank_volume:
            raise ValueError('Can not add more than tank volume')
        self.fuel_in_tank += volume

    def donate_fuel(self, volume: float, recipient: 'Vehicle'):
        if self.fuel_in_tank < volume:
            raise ValueError('Not enough fuel')
        recipient.fuel_add(volume)
        self.fuel_in_tank -= volume

    @abstractmethod
    def __str__(self):
        ...


class Car(Vehicle):

    def __init__(self, number_of_passengers: int, airbags: bool, brand: str, tank_volume: float,
                 fuel_in_tank: float, speed: float, mileage: float):
        super().__init__(brand=brand, tank_volume=tank_volume, fuel_in_tank=fuel_in_tank, speed=speed, mileage=mileage)
        self.number_of_passengers = number_of_passengers
        self.airbags = airbags

    def __str__(self) -> str:
        return (
            f"Марка: {self.brand}\n"
            f"Об'єм баку: {self.tank_volume} л\n"
            f"Залишок палива: {self.fuel_in_tank} л\n"
            f"Швидкість: {self.speed} км/год\n"
            f"Пробіг: {self.mileage} км\n"
        )


class Motorcycle(Vehicle):
    def __init__(self, side_seat: bool, brand: str, tank_volume: float, fuel_in_tank: float,
                 speed: float, mileage: float):
        super().__init__(brand=brand, tank_volume=tank_volume, fuel_in_tank=fuel_in_tank, speed=speed, mileage=mileage)
        self.side_seat = side_seat

    def __str__(self) -> str:
        return (
            f"Марка: {self.brand}\n"
            f"Об'єм баку: {self.tank_volume} л\n"
            f"Залишок палива: {self.fuel_in_tank} л\n"
            f"Швидкість: {self.speed} км/год\n"
            f"Пробіг: {self.mileage} км\n"
        )


car = Car(
    number_of_passengers=5, airbags=False, brand='Dodge',
    tank_volume=60, fuel_in_tank=30, speed=90, mileage=30000
)
moto = Motorcycle(
    side_seat=True, brand='Honda', tank_volume=80,
    fuel_in_tank=47, speed=50, mileage=15000
)

print(car)
print(moto)
car.donate_fuel(15, moto)
moto.fuel_add(10)
print(car)
print(moto)
