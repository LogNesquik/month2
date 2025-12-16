class Car:
    car_total = 0

    def __init__(self, model, speed):
        if Car.validate_speed(speed):
            self.model = model
            self.speed = speed
            Car.car_total += 1

    def drive(self):
        print(f"Car {self.model} speed: {self.speed}")

    @classmethod
    def test(cls):
        print("test ", cls.car_total)

    @classmethod
    def get_count(cls):
        # нет доступа к атрибутам.методам объектов
        # print(cls.model) # ошибка
        # cls.drive() # error
        print(f"{cls.car_total}")
        print(f"Всего {Car.car_total} машин")
        cls.test()
        Car.validate_speed(100)


    @staticmethod
    def validate_speed(val):
        if val < 0:
            raise ValueError("Value must be positive")
        return True

print(Car.car_total)
car_subaru = Car('subaru', 125)
print(Car.car_total)
car_honda = Car('honda', 115)
print(Car.car_total)

Car.get_count()
car_honda.drive()