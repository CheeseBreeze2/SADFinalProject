import os
import sqlite3 as sql

if os.path.exists('reservation.db'):
    os.remove('reservation.db')
    print("Existing database removed successfully")

conn = sql.connect('reservation.db')
print("New database created successfully")

conn.execute('CREATE TABLE reservations (name TEXT, checkIn DATE, checkOut DATE, roomType TEXT)')
print("Table created successfully")

conn.close()