"""
    Работа с СУБД SQLite3 по протоколу ODBC
"""



import pyodbc



DB_NAME = "my.db"

# Открытие соединения
odbc_connection = pyodbc.connect("DRIVER=SQLite3;DATABASE={db_name}".format(
    db_name = DB_NAME
))
cursor = odbc_connection.cursor()

# Создание таблиц
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Author (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(64) NOT NULL,
        age INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Book (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(32) NOT NULL,
        year  INTEGER NOT NULL,
        price INTEGER NOT NULL,

        author_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES Author(id)
    );
""")
odbc_connection.commit()

# Заполнение таблиц
cursor.execute("""
    INSERT INTO Author (name, age)
    VALUES ('Ivan', 34);
""")
cursor.execute("""
    INSERT INTO Author (name, age)
    VALUES ('John', 45);
""")
cursor.execute("""
    INSERT INTO Author (name, age)
    VALUES ('Jordan', 24);
""")
cursor.execute("""
    INSERT INTO Book (title, price, year, author_id)
    VALUES ('Moon light in the dark', 200, 1980, 1);
""")
cursor.execute("""
    INSERT INTO Book (title, price, year, author_id)
    VALUES ('Computer science for all', 99, 2017, 2);
""")
odbc_connection.commit();

# Выборка данных из БД
data = cursor.execute("""
    SELECT
        Book.id,
        title,
        price,
        year,
        Author.id,
        name,
        age
    FROM Book INNER JOIN Author
    ON Book.id = Author.id
""")
for i, row in enumerate(data.fetchall()):
    print("#{number} {title} | {name} | {year}".format(
        number=i + 1,
        title=row.title,
        name=row.name,
        year=row.year
    ))


# Закрытие соединения
odbc_connection.close()
