class Animal:
    def move(self):
        print("двигается")

class Swimming(Animal):
    def move(self):
        print("плавает")

class Flying(Animal):
    def move(self):
        print("летает")


class Duck(Swimming, Flying):
    pass


duck = Duck()
duck.move()

# Комит, для более красивого отображения изменений в гите.