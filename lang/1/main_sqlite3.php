<?php

// Открытие соединения с СУБД
$sqlite3 = new SQLite3("my.db");


// Создание таблиц
$query = <<<SQL
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
SQL;
$sqlite3->exec($query);


// Заполнение БД информацией
$query = <<<SQL
    INSERT INTO Author (name, age)
    VALUES ('Ivan', 34);

    INSERT INTO Author (name, age)
    VALUES ('John', 45);

    INSERT INTO Author (name, age)
    VALUES ('Jordan', 24);

    INSERT INTO Book (title, price, year, author_id)
    VALUES ('Moon light in the dark', 200, 1980, 1);

    INSERT INTO Book (title, price, year, author_id)
    VALUES ('Computer science for all', 99, 2017, 2);
SQL;
$sqlite3->exec($query);


// Выборка данных из БД
$query = <<<SQL
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
SQL;
$result = $sqlite3->query($query);


// Вывод информации
print("№ TITLE NAME YEAR\n");
$number = 1;
while ($record = $result->fetchArray(SQLITE3_ASSOC)) {
    print("#${number} ${record['title']} | ${record['name']} | ${record['year']}\n");
    $number++;
}


// Закрытие соединения
$sqlite3->close();
