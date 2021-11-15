import sqlite3

# conn = sqlite3.connect(':memory:') uses the database in memeory but doesnt save it. deletes at 
# the end of the program. 
conn = sqlite3.connect('customer.db')

