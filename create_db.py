import sqlite3 as sql

conn = sql.connect('reservation.db')
print("Opened database successfully")

conn.execute('CREATE TABLE reservations (name TEXT, checkIn INT, checkOut INT, roomType TEXT)')
print("Table created successfully")

conn.close()