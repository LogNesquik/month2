"""
Изначально идет допольнительно задание после основная домашняя задача.
Для дополнительного задания я использовал нейросеть чтобы получить информацию о datetime, как он работает и как его использовать.
На протяжении всего кода буду его комментировать, чтобы доказать что я сам писал код, а не нейронка.
"""

from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name # публичный атрибут
        self.__birth_date = datetime.strptime(birth_date, "%d.%m.%Y")  # приватный атрибут, в котором дата рождения преобразуется из строки в объект datetime для работы с датами
        self.__occupation = occupation # приватный атрибут
        self.__higher_education = higher_education # приватный атрибут
    
    # Метод для получения значения приватного атрибута occupation(тут @property не использовал, т.к в задании нужно было реализовать геттеры)
    @property
    def occupation(self):
        return self.__occupation
    
    
    # Метод для получения значения приватного атрибута higher_education(тут @property не использовал, т.к в задании нужно было реализовать геттеры)
    
    @property
    def higher_education(self):
        return self.__higher_education

    # Это тот же самый геттер, но с использованием декоратора 
    @property
    def birth_date(self):
        return self.__birth_date
    
    # Используем @property чтобы создать геттер для вычисляемого атрибута age
    @property
    def age(self): # Метод для вычисления возраста на основе даты рождения
        today = datetime.today() # Получаем текущую дату
        age = today.year - self.__birth_date.year # Вычисляем разницу в годах
        # Проверяем, был ли уже день рождения в этом году, чтобы предотвратить ошибку в возрасте
        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
            age -= 1 # Если день рождения еще не наступил в этом году, уменьшаем возраст на 1
        return age # Возвращаем вычисленный возраст

    # Метод introduce использует геттеры для доступа к приватным атрибутам
    def introduce(self):
        edu_text = 'есть' if self.higher_education else "нету"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, "
              f"по профессии {self.occupation()}, высшего образования {edu_text}.")

# Дочерние классы        
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, friend_of): 
        super().__init__(name, birth_date, occupation, higher_education)
        occupation = self.occupation # получение значения приватного атрибута через геттер(т.е мы назначаем значение приватного атрибута в родительнском классе через геттеры)
        higher_education = self.higher_education # получение значения приватного атрибута через геттер(т.е мы назначаем значение приватного атрибута в родительнском классе через геттеры)
        self.group_name = group_name # публичный атрибут
        self.friend_of = friend_of # публичный атрибут

    # Метод introduce использует геттеры для доступа к приватным атрибутам    
    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Я учился с {self.friend_of} в группе {self.group_name}. У меня {'есть' if self.higher_education else 'нету'} высшее образование.")
        
# Дочерний класс
class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_of=None):
        super().__init__(name, birth_date, occupation, higher_education)
        occupation = self.occupation # получение значения приватного атрибута через геттер(т.е мы назначаем значение приватного атрибута в родительнском классе через геттеры)
        higher_education = self.higher_education # получение значения приватного атрибута через геттер(т.е мы назначаем значение приватного атрибута в родительнском классе через геттеры)
        self.hobby = hobby # публичный атрибут
        self.friend_of = friend_of # публичный атрибут

    # Метод introduce использует геттеры для доступа к приватным атрибутам
    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Мое хобби {self.hobby}. У меня {'есть' if self.higher_education else 'нету'} высшее образование.")


cl1 = Classmate("Иван", "20.02.1999", "студент", True, "11D", "Айсулуу")
cl1.introduce() # Привет, меня зовут Иван. Моя профессия студент. Я учился с Айсулуу в группе 11D. У меня есть высшее образование.
fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce() # Привет, меня зовут Айбек. Моя профессия студент. Мое хобби футбол. У меня есть высшее образование.
print(fr1.age) # 25
print(cl1.age) # 26

"""
Комментарии я сам писал специально, т.к разбирал код из-за того что опоздал на половину урока.
ЭТО НЕ НЕЙРОНКА :)))


Надеюсь что все правильно и понятно объяснил
Ну воды я налил конечно много, но это чтобы показать что я сам писал код )
Спасибо за понимание!)
"""



