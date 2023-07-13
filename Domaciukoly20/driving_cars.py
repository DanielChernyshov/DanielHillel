import time
import random


class Car:
    def __init__(self, economy, color, model, mileage=0, fuel=100):
        self._mileage = mileage
        self._fuel = fuel
        self._economy = economy
        self._color = color
        self._model = model

    def drive(self, distance):
        for i in range(int(distance)):
            if self._fuel == 0:
                print("No fuel left!")
                break
            elif self._fuel < self._economy:
                print("Not enough fuel!")
                self._fuel = 0
                break
            else:
                self._fuel -= self._economy
                time.sleep(1)
                print("Driving...")
                break
        self._mileage += distance

    def distance_left(self):
        return self._fuel / self._economy * 100

    def fuel_up(self):
        self._fuel += 20

    @property
    def fuel(self):
        return self._fuel

    @property
    def model(self):
        return self._model

    @property
    def economy(self):
        return self._economy

    @property
    def color(self):
        return self._color

    @property
    def mileage(self):
        return self._mileage


models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
colors = ["blue", "green", "yellow", "black", "red", "green"]

cars = []

for _ in range(10):
    cars.append(
        Car(random.randrange(4, 20), random.choice(colors), random.choice(models))
    )

for item in cars:
    item.drive(200)
    item.fuel_up()
    item.drive(100)

max_fuel = max(cars, key=lambda car: car.fuel)

print(
    f"Your car has this much fuel: {max_fuel.fuel}. The economy is {max_fuel.economy}."
    f"The model is {max_fuel.model}. The mileage is {max_fuel.mileage}. The color is {max_fuel.color}"
)
