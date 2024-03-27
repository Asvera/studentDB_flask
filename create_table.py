# Description: This python script assumes that you already have a database.db
# Execute this python script before testing or editing this app code. 
# python create_table.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, zip TEXT)')
print("Created table successfully!")

conn.close()

