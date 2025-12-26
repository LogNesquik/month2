# https://www.notion.so/Homework-2-227223aba87d80fe8fa4d5a0f141c8a3
class Person:
    def __init__(self, name, birth_date, occupation, education):
        self.name = name
        self.birth_date = birth_date
        self.occu = occupation
        self.edu = education

    def intoroduce(self):
        print(f"Меня зовут {self.name}. Я родился в {self.birth_date}. Я работаю {self.occu}. Я закончил {self.edu}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, education, group_name):
        super().__init__(name, birth_date, occupation, education)
        self.group_name = group_name

    def introduce(self):
        print(f"Меня зовут {self.name}. Я родился в {self.birth_date}. Я работаю {self.occu}. Я закончил {self.edu}. Группа - {self.group_name}")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, education, hobby):
        super().__init__(name, birth_date, occupation, education)
        self.hobby = hobby 

    def introduce(self):
        print(f"Меня зовут {self.name}. Я родился в {self.birth_date}. Я работаю {self.occu}. Я закончил {self.edu}. Хобби - {self.hobby}")


friend = Friend("Алмаз", "5.12.2000", "программистом", True, "футбол")
friend.introduce()

classmate = Classmate('Бектур', '5.12.2000', 'программистом', False, '10Б')
classmate.introduce()
