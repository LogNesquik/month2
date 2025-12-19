"""
Docstring for my_proggrams.Mentorstvo
Это модуль, содержащий функции и классы, связанные с программой наставничества
Он будет мне помогать в нахождении и управлении учеников и их прогрессом
Всю информацию будет вводить пользователь, будем использовать консольный ввод-вывод, разноцветный текст в консоли

Т.к на месяц даются одни и те же задания, и одни и те же ученики, то можно будет сохранять пользователь просто в список внутри проекта
Буду использовать словарь для хранения информации об учениках и их прогрессе
После изучение базы данных, можно будет сохранять информацию в файл или базу данных

Пока что реализую базовые функции:
- Добавление ученика +
- Удаление ученика

- Просмотр списка учеников
- Обновление прогресса ученика

- Вывод прогресса всех учеников
- Запись в словарь и чтение из словаря



В будущем можно будет добавить:
- Поиск ученика по имени или другим параметрам
- Фильтрация учеников по уровню прогресса
- Генерация отчетов о прогрессе учеников
- Сохранение и загрузка данных из файла (в будущем)
"""

from blessed import Terminal

term = Terminal()

class Mentorstvo:
    # Записываю тг юзы, и имена учеников в словарь
    students = {
        '@Beksultan183': 'Бексултан Сейитбеков',
        '@olimhuzha': 'Олимхужа',
        '@zoldikr': 'Миша',
        '@linasenbye': 'Элина',
        '@medelen7': 'Медина',
        '@Pss_kr09': 'Искендер',
        '@Tiubeev_tilek': 'Тилек'
    }

    count = 0

    @classmethod
    def display_students(cls):
        print(term.bold_uderline('Список учеников:'))
        for tg_username, name in cls.students.items():
            print(f'{term.cyan}{name} - {term.green}{tg_username}')

    @classmethod
    def add_student(cls, tg_username, name):
        if tg_username in cls.students:
            print(term.red('Ученик с таким тг юзером уже существует!'))
        else:
            cls.students[tg_username] = name
            print(term.green(f'Ученик {name} успешно добавлен!(К сожалению пока без сохранения в файл)'))
            cls.count += 1

    @classmethod
    def remove_student(cls, tg_username):
        if tg_username not in cls.students:
            print(term.red('Ученик с таким тг юзером не найден!'))
        else:
            cls.students.pop(tg_username)
            print(term.green(f'Ученик с тг юзером {tg_username} успешно удален!(К сожалению пока без сохранения в файл)'))
            cls.count -= 1

    @classmethod
    def counter(cls):
        cls.count = 0
        for tg_username, name in cls.students.items():
            cls.count += 1
        print(term.bold_underline(f'Всего учеников: {cls.count}'))
        return cls.count
    
if __name__ == "__main__":
    while True:
        line = input("Введите команду (add, remove, display, count, exit): ").strip().lower()

        if line == 'exit':
            print(term.bold_underline('Выход из программы наставничества.'))
            break

        if line == 'add':
            tg_username = input("Введите тг юзер ученика: ").strip()
            name = input("Введите имя ученика: ").strip()
            Mentorstvo.add_student(tg_username, name)
        elif line == 'remove':
            tg_username = input("Введите тг юзер ученика для удаления: ").strip()
            Mentorstvo.remove_student(tg_username)
        elif line == 'display':
            Mentorstvo.display_students()
        elif line == 'count':
            print(term.bold_underline('Подсчет учеников: '))
            Mentorstvo.counter()
        else:
            print(term.red("Неизвестная команда!"))

