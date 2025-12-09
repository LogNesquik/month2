class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @name.setter
    def name(self, new_name):
        self.__name = new_name


    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
cat = Cat("Whiskers", 3)
dog = Dog("Buddy", 5)

print(f"{cat.name} says {cat.make_sound()}\n")
print(f"{dog.name} says {dog.make_sound()}\n")

cat.age = 4
dog.age = 6
cat.name = "Mittens"
dog.name = "Max"

print(f"{cat.name} is now {cat.age} years old.")
print(f"{dog.name} is now {dog.age} years old.")


animals = [cat, dog]
print("\n=== Демонстрация полиморфизма ===")
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")