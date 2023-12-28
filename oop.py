import subprocess
from time import sleep


class Car:
    CAR_MILAGE = 0

    def __init__(self, manufacturer: str, brand: str, fuel_consumption: float, year: int = 2020):
        self.year = year
        self.manufacturer = manufacturer
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.car_mileage = Car.CAR_MILAGE

    def __str__(self) -> str:
        return (
            f'В тебе крута машина, це {self.manufacturer.title()} '
            f'яку компанія {self.brand.title()} випустили в {self.year}?'
        )

    def apply_signal(self):
        subprocess.run(["say", '"обережно, там тупик"'])


car_1 = Car('Honda', 'Honda Motor', 11)
car_2 = Car('DODGE', 'craysler', 10.5)

print(car_1)
print(car_2)
sleep(1)
car_1.apply_signal()
