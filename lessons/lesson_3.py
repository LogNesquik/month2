class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False
        self.__max_speed = 100
        self.test = None


    def drive_to(self, destination):
        print(f"Max speed: {self.__max_speed}")
        self.__max_speed += 1
        if self._fined:
            print("Fined")
            return
        print(f"Car {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

    def __test(self):
        print(f"Car {self.model} test")


    # геттер
    def get_max_speed(self):
        return self.__max_speed

    # сеттер
    def set_max_speed(self, value):
        if value <= 0:
            raise ValueError("Max speed must be positive")
        self.__max_speed = value


    @property
    def max_speed(self):
        return self.__max_speed


    @max_speed.setter
    def max_speed(self, value):
        if value <= 0:
            raise ValueError("Max speed must be positive")

        self.__max_speed = value


car_honda = Car(color = "red", model = "Honda")
car_subaru = Car(color = "blue", model = "Subaru")
car_subaru.drive_to("Karakol")
car_subaru.drive_to("Karakol")
print(car_honda.color)
print(car_subaru._fined)

# ошибка
# print(car_subaru.__max_speed)
# car_subaru.__test()
# Ошибка, так как атрибут приватный
# Лайфхак, но не стоит использовать
# print(car_subaru._Car__max_speed)

print(f"{car_subaru.model} max speed:",
      car_subaru.get_max_speed())
car_subaru.set_max_speed(140)
print(f"{car_subaru.model} max speed:",
      car_subaru.get_max_speed())

print(car_honda.max_speed)
car_honda.max_speed = 100
print(car_honda.max_speed)