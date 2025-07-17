#!/usr/bin/env python3
"""
Fixed Flask application with security vulnerabilities and performance issues resolved
"""
import sqlite3
import hashlib
import time
import os
from flask import Flask, request, render_template_string, session, redirect, url_for
from markupsafe import escape
import bcrypt

app = Flask(__name__)
# FIX: Use environment variable for secret key instead of hardcoded value
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

# FIX #1: SQL Injection vulnerability - Use parameterized queries
def get_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # FIXED: Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

# FIX #2: Performance Issue - Optimized O(n) algorithm instead of O(n²)
def find_duplicates(numbers):
    """
    Optimized duplicate finder using hash set for O(n) time complexity
    instead of the previous O(n²) nested loop approach
    """
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

def hash_password(password):
    """
    IMPROVED: Use bcrypt instead of MD5 for secure password hashing
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed):
    """
    Verify password against bcrypt hash
    """
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except:
        return False

@app.route('/')
def index():
    return render_template_string('''
    <h1>Welcome to the Demo App (Fixed Version)</h1>
    <a href="/login">Login</a> | <a href="/search">Search Users</a> | <a href="/process">Process Data</a>
    ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Input validation
        if not username or not password:
            return "Username and password are required"
        
        user = get_user(username, password)
        if user:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Login failed"
    
    return render_template_string('''
    <form method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
    ''')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    # Use escape to prevent any potential XSS in session data
    return f"Welcome {escape(session['user'])}!"

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        # FIX #3: XSS vulnerability - Use proper template rendering with automatic escaping
        return render_template_string('<h1>Search Results for: {{ query }}</h1>', query=query)
    
    return render_template_string('''
    <form>
        Search: <input type="text" name="q">
        <input type="submit" value="Search">
    </form>
    ''')

@app.route('/process')
def process_data():
    # Demonstrate the performance improvement with the fixed algorithm
    numbers = list(range(1000)) + [1, 2, 3, 1, 2, 3]  # Add some duplicates
    start_time = time.time()
    duplicates = find_duplicates(numbers)
    end_time = time.time()
    
    return f"Found duplicates: {duplicates}. Processing took {end_time - start_time:.6f} seconds (OPTIMIZED)"

# Additional security improvements
@app.after_request
def add_security_headers(response):
    """Add security headers to all responses"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

if __name__ == '__main__':
    # Initialize database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    
    # Insert test user with secure password hashing
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                       ('admin', hash_password('password123')))
    except sqlite3.IntegrityError:
        pass  # User already exists
    
    conn.commit()
    conn.close()
    
    # FIXED: Don't run in debug mode in production
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)