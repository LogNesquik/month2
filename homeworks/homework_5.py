class Vehicle:
    def start(self):
        print("vehicle started")


class Car(Vehicle):
    def start(self):
        super().start()
        print("car started")

class ElectricCar(Vehicle):
    def start(self):
        super().start()


class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print("tesla ready")

tesla = Tesla()
tesla.start()
print(Tesla.mro())
# Комит, для более красивого отображения изменений в гите.