# https://six-smartphone-1ca.notion.site/Homework-1-242223aba87d80f29621e387a92d51af

class Person:
    def __init__(self, name, birth_date, occupation, education):
        self.name = name
        self.birth_date = birth_date
        self.occu = occupation
        self.edu = education

    def intoroduce(self):
        print(f"Меня зовут {self.name}. Я родился в {self.birth_date}. Я работаю {self.occu}. Я закончил {self.edu}")

a = Person("Miroslav", "1999", "programmer", "high school", )
b = Person("Artur", "2000", "student", "university")

a.intoroduce()
b.intoroduce()