# Database Programming in Python
# You should know SQL before this class!

# Create a connection with the database
import sqlite3

# Objected-oriented programming
class Person:
    def __init__(self, id_number=-1, first_name="", last_name="", age=-1):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    # Define a method which loads a data

    def load_person(self, id_number):
        self.cursor.execute("""
            SELECT * FROM person WHERE id_number = ?
        """, (id_number,))

        results = self.cursor.fetchone() # get a tuples of the first element

        self.id_number = results[0]
        self.first_name = results[1]
        self.last_name = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute("""
            INSERT INTO person (id_number, first_name, last_name, age) VALUES
            (?, ?, ?, ?)
        """, (self.id_number, self.first_name, self.last_name, self.age))

        self.connection.commit()

connection = sqlite3.connect('mydata.db') #generate mydata.db file
cursor = connection.cursor() # Control command on the database

# Drop table
cursor.execute("""DROP TABLE IF EXISTS person""")

# Create Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS person (
        id_number INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(32),
        last_name VARCHAR(32),
        age INTEGER
    )
""")

# Insert Table
cursor.execute("""
    INSERT INTO person (id_number, first_name, last_name, age) VALUES
    (01, 'Paul', 'Smith', 24),
    (02, 'Mark', 'Johnson', 42),
    (03, 'Anna', 'Smith', 34)
""")

# Select the ALL content and find 'Smith'
cursor.execute("""
    SELECT * FROM person
    WHERE last_name = 'Smith'
""")

rows = cursor.fetchall() # get all
print(rows)

connection.commit() # To execute the scripts
connection.close()

# ========== Improvised ==========

p1 = Person()
p1.load_person(2) #default
print(f" Name: {p1.first_name}")
print(f" Surname: {p1.last_name}")
print(f" Age: {p1.age}")
print(f" Number: {p1.id_number}")

# Manually added on the table

new_entries = [
    (7, "Leon", "Kennedy", 51),
    (8, "Grace", "Ashcroft", 24),
    (9, "Victor", "Gideon", 99)
]

for data in new_entries:
    p = Person(*data) # * add the data

    # * = The Splat Operator for more clean code:
    # stop writing data[0], data[1]
    # Pour it down automatically on the lists
    # and unpacking it

    p.insert_person() # every data that added on insert_person() fn

print("\n===== FINAL UPDATE IN DATABASE =====")
p.cursor.execute(""" SELECT * FROM person""")
for person in p.cursor.fetchall():
    print(person)