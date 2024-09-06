class Car:
    def __init__(self, make, model, year):
        # Initialize the attributes/instance variables
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Print out the car's information
        print(f"Car Details: {self.year} {self.make} {self.model}")

my_car = Car("Nissan", "xtrail", 2022)#creates an instance by calling __init__
my_car.display_info()
