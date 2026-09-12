class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} vehicle is starting.")

    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):
    def __init__(self, brand, number_of_doors):
        super().__init__(brand)
        self.number_of_doors = number_of_doors

    def move(self):
        print(
            f"The {self.brand} car is driving "
            f"on four wheels."
        )


class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

    def move(self):
        print(
            f"The {self.brand} {self.bike_type} bike "
            f"is travelling on two wheels."
        )


# Create objects
vehicle = Vehicle("Generic")
car = Car("Toyota Land Cruiser", 4)
bike = Bike("Yamaha", "sports")

# Call the base-class method
vehicle.start()
vehicle.move()

print()

# Call inherited and overridden methods
car.start()
car.move()
print("Number of doors:", car.number_of_doors)

print()

bike.start()
bike.move()
print("Bike type:", bike.bike_type)