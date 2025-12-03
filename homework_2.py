class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
        
    def introduce(self):
        edu_text = 'есть' if self.higher_education else "нету"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии {self.occupation}, высшего образования {edu_text}.")
        
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, friend_of=None):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
        self.friend_of = friend_of
    
    def introduce(self):
        print(f"Привет меня зовут {self.name}, я одноклассник {self.friend_of}, я родился {self.birth_date}, работаю {self.occupation}")
        

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_of=None):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_of = friend_of

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я друг {self.friend_of}, я родился {self.birth_date}, работаю {self.occupation}")

friend = Friend("Алмаз", "5.12.2000", "программистом", True, "футбол", "Байэля")
friend.introduce()

classmate = Classmate('Бектур', '5.12.2000', 'программистом', False, '10Б', 'Байэля')
classmate.introduce()
print("----------------------")


people_objects = [
    Friend("Елена", "12.04.1997", "врачом", True, "танцы", "Насти"),
    Classmate("Петр", "03.09.2002", "студентом", False, "9Б", "Игоря"),
    Person("Ева", "18.07.1985", "учителем", True)
]

for person in people_objects:
    person.introduce()

print("----------------------")
class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_of=None, shared_memory=None):
        super().__init__(name, birth_date, occupation, higher_education, hobby, friend_of)
        self.shared_memory = shared_memory 

    def introduce(self):
        super().introduce()
        if self.shared_memory:
            print(f"Мы с {self.friend_of} вместе пережили: {self.shared_memory}")


best_friend = BestFriend("Алексей", "10.10.1995", "инженером", True, "рыбалка", "Ивана", "поездку на Байкал")
best_friend.introduce()