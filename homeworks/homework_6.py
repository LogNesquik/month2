from blessed import Terminal

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