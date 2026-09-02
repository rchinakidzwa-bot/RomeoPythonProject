class Car:
    def __init__(self, make: object, model: object, year: object) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Brand: {self.make}, Model: {self.model}, Year: {self.year}")

cars = []

while True:
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")

    car = Car(make, model, year)
    cars.append(car)

    choice = input("Add another car? (yes/no): ").lower()
    
    if choice != "yes":
        break
        
    print("\n--- Car Details ---")
    for car in cars:  
        car.display()


