import sqlite3


# To initialize a database connection:
####################################################
connection = sqlite3.connect('database_test_example.db')

cursor = connection.cursor()

# Uncomment and run code to show all db entries
####################################################
cursor.execute("""
SELECT * FROM persons
""")

rows = cursor.fetchall()
print(rows)

connection.commit()

connection.close()

####################################################
#
#
#
#
#
#
#
#
#
#
#
#
#
# Class definition essentially compiled from code below
####################################################
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons (
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER)
# """)
#
# cursor.execute("""
# INSERT INTO persons VALUES
# (567, 'Ben', 'Dover', 57),
# (678, 'Jack', 'MeHoff', 40)
# """)

# cursor.execute("""
# SELECT * FROM persons
# WHERE last_name = 'Dover'
# # """)