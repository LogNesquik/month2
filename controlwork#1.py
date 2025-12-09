class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age
    
    def make_sound(self):
        return "Животное издает звук"


class Dog(Animal):
    def make_sound(self):
        return "гав гав гав!"


class Cat(Animal):
    def make_sound(self):
        return "мяу мяу мяу!"


# Создание и использование объектов
dog = Dog("Шарик", 3)
cat = Cat("Мурка", 2)

# Использование геттеров (property)
print(f"Имя собаки: {dog.name}, Возраст собаки: {dog.age}")
print(f"Возраст кота: {cat.age}, Имя кота: {cat.name}")

# Демонстрация полиморфизма
animals = [dog, cat]
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")

# Использование сеттеров
dog.name = "Бобик"
cat.age = 4

print(f"\nПосле изменений:")
print(f"Собака: {dog.name} - {dog.make_sound()}")
print(f"Кот: {cat.name} - {cat.make_sound()}")