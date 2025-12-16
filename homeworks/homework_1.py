class Person:
    # Инициализация публичных атрибутов
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
        
    def introduce(self):
        edu_text = 'есть' if self.higher_education else "нету"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии {self.occupation}, высшего образования {edu_text}.")
              
friend_artyr = Person('Артур', '25.06.11', 'Беспилотник', False)
friend_ratmir = Person('Ратмир', '14.02.11', 'Повар', False)
friend_eva = Person('Ева', '08.08.11', 'Теннисистка', True)

print(friend_artyr.name, friend_artyr.birth_date, friend_artyr.occupation, friend_artyr.higher_education)
print(friend_ratmir.name, friend_ratmir.birth_date, friend_ratmir.occupation, friend_ratmir.higher_education)
print(friend_eva.name, friend_eva.birth_date, friend_eva.occupation, friend_eva.higher_education)

friend_artyr.introduce()
friend_ratmir.introduce()
friend_eva.introduce()