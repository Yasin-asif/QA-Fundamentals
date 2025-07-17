#!/usr/bin/env python3
"""
Sample Flask application with intentional bugs for demonstration
"""
import sqlite3
import hashlib
import time
from flask import Flask, request, render_template_string, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret"  # Bug 1: Hardcoded secret key (Security vulnerability)

# Bug 2: SQL Injection vulnerability
def get_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Vulnerable SQL query - directly inserting user input
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

# Bug 3: Inefficient algorithm with O(n²) complexity
def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates

def hash_password(password):
    # Using MD5 which is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()

@app.route('/')
def index():
    return render_template_string('''
    <h1>Welcome to the Demo App</h1>
    <a href="/login">Login</a> | <a href="/search">Search Users</a> | <a href="/process">Process Data</a>
    ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = get_user(username, password)
        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Login failed"
    
    return render_template_string('''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    ''')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return f"Welcome {session['user']}!"

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        # Potential XSS vulnerability - rendering user input directly
        return render_template_string(f'<h1>Search Results for: {query}</h1>')
    return render_template_string('''
    <form>
        Search: <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
    ''')

@app.route('/process')
def process_data():
    # Simulate processing large dataset with inefficient algorithm
    numbers = list(range(1000)) + [1, 2, 3, 1, 2, 3]  # Add some duplicates
    start_time = time.time()
    duplicates = find_duplicates(numbers)
    end_time = time.time()
    
    return f"Found duplicates: {duplicates}. Processing took {end_time - start_time:.4f} seconds"

if __name__ == '__main__':
    # Initialize database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    
    # Insert test user with weak password hashing
    cursor.execute("INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)", 
                   ('admin', hash_password('password123')))
    conn.commit()
    conn.close()
    
    app.run(debug=True, host='0.0.0.0')  # Bug: Debug mode in production