import sqlite3


class Person:
    def __init__(self, id_num=-1, first="", last="", age=-1):
        self.id_num = id_num
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('database_test_example.db')
        self.cursor = self.connection.cursor()

    def load_all(self):
        self.cursor.execute(""" 
        SELECT * FROM persons
        """)
        return self.cursor.fetchall()

    def load_person(self, id_num):
        self.cursor.execute(f"""
        SELECT * FROM persons
        WHERE id = {id_num}
        """)

        results = self.cursor.fetchone()

        self.id_num = id_num
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute(f"""
        INSERT INTO persons VALUES
        ({self.id_num}, '{self.first}', '{self.last}', {self.age})
        """)
        self.connection.commit()
        self.connection.close()
