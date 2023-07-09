import time

class Car:
    def __init__(self, economy, color, model, mileage=0, fuel=100, **kwargs):
        super().__init__(**kwargs)
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
                self._fuel=0
                break
            else:
                self._fuel -= self._economy
                time.sleep(1)
                print("Driving...")
                break
        self._mileage += distance

    def distance_left(self):
        return self._fuel / self._economy

    def fuel_up(self):
            self._fuel += 20

import random
models = ['Toyota', 'Honda', 'Ford', 'Chevrolet','Nissan']
colors = ['blue','green','yellow','black','red','green']

cars = []

for i in range(10):
    cars.append(Car(random.randrange(100), random.choice(colors), random.choice(models)))

for item in cars:
    item.drive(200)
    item.fuel_up()
    item.drive(100)


from operator import attrgetter


max_fuel = max(cars, key=attrgetter('_fuel'))
print(f"The car with the most fuel has {max_fuel._fuel} fuel, the economy is {max_fuel._economy}, "
      f"the color of the car is {max_fuel._color}, the model of the car is {max_fuel._model}")