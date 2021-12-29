import sqlite3
from sqlite3.dbapi2 import connect

# conn = sqlite3.connect(':memory:') uses the database in memeory but doesnt save it. deletes at 
# the end of the program. 
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()


# Query and Return all records from DB
def show_all():
    conn = sqlite3.connect('customer.db')

    # create a cursor
    c = conn.cursor()
    # Query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)
    # Commit commands
    conn.commit()
    # Close the connection
    conn.close()


# Add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')

    # create a cursor
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    # Commit commands
    conn.commit()
    # Close the connection
    conn.close()

def add_many(list):
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

#  Delete Record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

# add_one("Laura", "Smith", "laura@smith.com")


#  create a table
# Datatypes in sqlite NULL, INT, REAL, TEXT, BLOB
# c.execute("""
#             CREATE TABLE customers (
#                 first_name TEXT,
#                 last_name TEXT,
#                 email TEXT
#             )

#         """)
#
# # Inserting into the Database
# c.execute("""
#             INSERT INTO customers VALUES ('John', 'Dow', 'john@doe.com')
#             """)
# many_customers = [('Wes', 'Brown', 'wes@brown.com'),
#                   ('Steph', 'Kuewa', 'steph@kuewa.com'),
#                   ('Dan', 'Pas', 'dan@pas.com')]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


# print(c.fetchone()[1])
# c.fetchmany(3)
# items = c.fetchall()
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()
c.execute("""
        DELETE FROM customers
        WHERE rowid IN (5,6,7)
        """)

conn.commit()