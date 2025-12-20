import sqlite3

conn = sqlite3.connect('books.db')

def create_table():
    """Создание таблицы books"""
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    conn.commit()

def insert_books():
    conn.execute("INSERT INTO books VALUES (1, 'Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея', 1225, 5)")
    conn.execute("INSERT INTO books VALUES (2, 'Преступление и наказание', 'Федор Достоевский', 1866, 'Психологический роман', 671, 3)")
    conn.execute("INSERT INTO books VALUES (3, 'Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Роман', 480, 4)")
    conn.execute("INSERT INTO books VALUES (4, '1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 6)")
    conn.execute("INSERT INTO books VALUES (5, 'Убить пересмешника', 'Харпер Ли', 1960, 'Роман', 376, 2)")
    conn.execute("INSERT INTO books VALUES (6, 'Гордость и предубеждение', 'Джейн Остин', 1813, 'Роман', 432, 4)")
    conn.execute("INSERT INTO books VALUES (7, 'Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 'Философская сказка', 96, 8)")
    conn.execute("INSERT INTO books VALUES (8, 'Гарри Поттер и философский камень', 'Дж.К. Роулинг', 1997, 'Фэнтези', 320, 7)")
    conn.execute("INSERT INTO books VALUES (9, 'Властелин колец', 'Дж.Р.Р. Толкин', 1954, 'Фэнтези', 423, 5)")
    conn.execute("INSERT INTO books VALUES (10, 'Алиса в Стране чудес', 'Льюис Кэрролл', 1865, 'Детская литература', 200, 6)")
    conn.commit()

if __name__ == '__main__':
    create_table()
    insert_books()