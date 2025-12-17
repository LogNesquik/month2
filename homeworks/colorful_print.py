from blessed import Terminal
from homework_1 import Person

term = Terminal()

fruct_color = {
    'apple': term.red,
    'banana': term.yellow,
    'cherry': term.magenta,
    'grape': term.purple,
    'orange': term.orange,
    'mango': term.bright_yellow,
    'peach': term.bright_magenta
}

print(term.bold_underline('Fruit Color Display'))
for fruit, color in fruct_color.items():
    print(color(fruit))


people = Person('Иван', '01.01.90', 'Инженер', True)
people_2 = Person('Мария', '15.05.85', 'Врач', False)
people_3 = Person('Алексей', '20.10.92', 'Учитель', True)
people.introduce()
people_2.introduce()
people_3.introduce()