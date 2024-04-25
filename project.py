from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_reservations():
    try:
        conn = sqlite3.connect('reservation.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM reservations")
        rows = cur.fetchall()
        conn.close()
        print("Reservation data fetched successfully:", rows)
        return rows
    except Exception as e:
        print("Error fetching reservation data:", e)
        return []

def insert_reservation(name, check_in, check_out, room_type):
    try:
        conn = sqlite3.connect('reservation.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO reservations (name, checkIn, checkOut, roomType) VALUES (?, ?, ?, ?)",
                    (name, check_in, check_out, room_type))
        conn.commit()
        conn.close()
        print("Reservation inserted successfully")
    except Exception as e:
        print("Error inserting reservation:", e)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    if request.method == 'POST':
        name = request.form['name']
        check_in = request.form['check_in']  # Corrected field name
        check_out = request.form['check_out']  # Corrected field name
        room_type = request.form['room_type']
        insert_reservation(name, check_in, check_out, room_type)
        return redirect(url_for('confirmation', name=name, checkin=check_in, checkout=check_out, room_type=room_type))
    return redirect(url_for('home'))  # Redirect to home if not a POST request


@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    checkin = request.args.get('checkin')
    checkout = request.args.get('checkout')
    return render_template('confirmation.html', name=name, checkin=checkin, checkout=checkout)

@app.route('/list')
def list():
    reservations = get_reservations()
    return render_template('list.html', reservations=reservations)

if __name__ == "__main__":
    app.run()
