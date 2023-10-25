class Vehicle:
    def __init__(self, speed, weight):
        self.speed = speed
        self.weight = weight
        self.mileage = 0

    def drive(self, distance):
        self.mileage += distance
        print(f"I drive {distance} km!")


class Car(Vehicle):
    def __init__(self, speed, weight, brand):
        super().__init__(speed, weight)
        self.brand = brand

    def drive(self, distance):
        self.mileage += distance
        print(f"I fly {distance} km!")


class Bicycle(Vehicle):
    def __init__(self, speed, weight, count_of_speeds):
        super().__init__(speed, weight)
        self.count_of_speeds = count_of_speeds

    def ride_on_back(self):
        print("WoooooW!")


bike = Bicycle(24, 20, 27)
bike.drive(10)

car = Car(120, "60 ton", "toyota")
car.drive(10 ** 5)

vehicles = [bike, car]
for vehicle in vehicles:
    print(vehicle.mileage)
