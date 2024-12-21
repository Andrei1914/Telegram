import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INT PRIMARY KEY NOT NULL,
        Title TEXT NOT NULL,
        Description TEXT,
        Price INT NOT NULL
        )
    ''')
    connection.commit()


def get_all_products():
    cursor.execute('''
    SELECT * FROM Products
    ''')
    return cursor.fetchall()


    # chek_user = cursor.execute("SELECT * FROM Products WHERE Title =?", (Title,))
    # if chek_user.fetchall() is None:
    #     cursor.execute(f'''
    #     INSERT INTO Users VALUES('{Title}','{Description}','{Price}')
    #     ''')
# cursor.execute("CREATE INDEX IF NOT EXISTS IDX_email ON Users(email)")
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users(Username, Email, Age, balance) VALUES(?, ?, ?, ?)", \
#     (f"User{i}", f"example{i}@gmail.com", int("10")*i, 1000))

# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", ("25", "newuser_0"))
# cursor.execute("DELETE FROM Users WHERE Id = ?", ("11", ))
# cursor.execute("SELECT Age, AVG(Age) FROM Users GROUP by Age")
# for i in range(1, 11):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 == 0", ("500", ))


# connection.commit()
# connection.close()