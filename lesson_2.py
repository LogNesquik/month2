# Родительский класс
class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"Car {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

# Дочерние классы
class Bus(Car):
    def __init__(self, color, model, number):
        super().__init__(color, model)
        self.number = number

class Truck(Car):
    def drive_to(self, destination):
        print(f"Truck {self.model} driving to {destination}")

    def test(self):
        print(f"Bus test method {self.model}")

truck_one = Truck('red', 'Mersedes')
truck_one.drive_to('Bishkek')
print(truck_one.color, truck_one.model)
bus_42 = Bus('yellow', 'Ikarus', 42)