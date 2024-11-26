from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')  # Connect to SQLite database
    cursor = conn.cursor()
    # Create the 'user' table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home route to display all users
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Retrieve all users from the database
    cursor.execute('SELECT * FROM user')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Route to handle adding a new user
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    address = request.form['address']
    email = request.form['email']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Insert new user into the database
    cursor.execute('INSERT INTO user (name, address, email) VALUES (?, ?, ?)', (name, address, email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to handle deleting a user
@app.route('/delete/<int:id>')
def delete_user(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Delete user by ID
    cursor.execute('DELETE FROM user WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to handle updating a user
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # Update user details in the database
        cursor.execute('UPDATE user SET name = ?, address = ?, email = ? WHERE id = ?', (name, address, email, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # Retrieve user details for editing
        cursor.execute('SELECT * FROM user WHERE id = ?', (id,))
        user = cursor.fetchone()
        conn.close()
        return render_template('update.html', user=user)

# Initialize database and run the application
if __name__ == '__main__':
    init_db()  # Ensure database and table are set up
    app.run(debug=True)
