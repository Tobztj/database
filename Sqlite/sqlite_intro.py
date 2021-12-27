import sqlite3

# conn = sqlite3.connect(':memory:') uses the database in memeory but doesnt save it. deletes at 
# the end of the program. 
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

#  create a table
# Datatypes in sqlite NULL, INT, REAL, TEXT, BLOB

# Inserting into the Database
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


# c.execute("""
#         DELETE FROM customers
#         WHERE rowid = 6
#         """)
c.execute("""
            SELECT rowid, * FROM
            customers
            LIMIT 2
            """)
items = c.fetchall()

for item in items:
    print(item)


# commit our command to the database
conn.commit()
# close the connection
conn.close()


