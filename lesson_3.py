class Car:
    def __init__(self, color, model,):
        self.color = color
        self.model = model
        self._find = False
        self.__max_speed = 0

    def drive_to(self, destination):

        print(f"Car {self.model} driving to {destination}")
    
    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

# отправлю полный код позже, когда выложат на гитхаб