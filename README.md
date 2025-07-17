# Bug Hunting and Fixing Project

## Overview
This project demonstrates the identification and resolution of three critical bugs in a Flask web application, showcasing common security vulnerabilities, performance issues, and coding errors found in real-world applications.

## Files in this Repository

### Original QA Documentation
- `SDLC_QA_Roles.md` - Software Development Life Cycle with QA roles
- `STLC_QA_Roles.md` - Software Testing Life Cycle documentation

### Bug Demonstration & Fixes
- `app.py` - Original Flask application with intentional bugs
- `app_fixed.py` - Corrected version with all bugs resolved
- `bug_analysis_and_fixes.md` - Detailed analysis of each bug and fix
- `performance_test.py` - Script demonstrating performance improvements
- `requirements.txt` - Python dependencies

## Three Critical Bugs Identified and Fixed

### 🔴 Bug #1: SQL Injection Vulnerability (CRITICAL)
- **Location**: `get_user()` function in `app.py`
- **Issue**: Direct string concatenation in SQL queries
- **Impact**: Complete authentication bypass and data exposure
- **Fix**: Implemented parameterized queries

**Before:**
```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

**After:**
```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

### 🟠 Bug #2: Performance Issue - O(n²) Algorithm (HIGH)
- **Location**: `find_duplicates()` function in `app.py`
- **Issue**: Nested loops causing quadratic time complexity
- **Impact**: Severe performance degradation with large datasets
- **Fix**: Hash-based algorithm with O(n) complexity

**Performance Improvement Results:**
```
Size       Buggy (O(n²))   Fixed (O(n))    Improvement    
------------------------------------------------------------
100        0.000454s       0.000008s       57.67x faster
500        0.013192s       0.000051s       259.77x faster
1000       0.051153s       0.000069s       742.39x faster
2000       0.201825s       0.000216s       934.35x faster
```

### 🟡 Bug #3: Cross-Site Scripting (XSS) Vulnerability (MEDIUM-HIGH)
- **Location**: `search()` function in `app.py`
- **Issue**: Direct rendering of user input without escaping
- **Impact**: Malicious script execution in user browsers
- **Fix**: Proper template rendering with automatic escaping

**Before:**
```python
return render_template_string(f'<h1>Search Results for: {query}</h1>')
```

**After:**
```python
return render_template_string('<h1>Search Results for: {{ query }}</h1>', query=query)
```

## Additional Security Improvements

1. **Secure Secret Key Management**: Environment variables instead of hardcoded values
2. **Strong Password Hashing**: bcrypt instead of MD5
3. **Security Headers**: Added XSS protection, frame options, and HSTS
4. **Input Validation**: Required field validation and sanitization
5. **Production Security**: Disabled debug mode in production

## How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Buggy Version (for demonstration)
```bash
python3 app.py
```

### Run the Fixed Version
```bash
python3 app_fixed.py
```

### Test Performance Improvements
```bash
python3 performance_test.py
```

## Testing the Vulnerabilities

### SQL Injection Test
Try logging in with:
- Username: `admin' OR '1'='1' --`
- Password: `anything`

### XSS Test
Visit: `http://localhost:5000/search?q=<script>alert('XSS')</script>`

### Performance Test
Visit: `http://localhost:5000/process` and observe processing times

## Security Best Practices Demonstrated

1. **Input Validation**: Always validate and sanitize user input
2. **Parameterized Queries**: Use prepared statements to prevent SQL injection
3. **Output Encoding**: Escape output to prevent XSS attacks
4. **Security Headers**: Implement proper HTTP security headers
5. **Password Security**: Use strong hashing algorithms like bcrypt
6. **Configuration Security**: Use environment variables for sensitive data

## Key Learnings

1. **Security-First Development**: Always consider security implications during development
2. **Performance Optimization**: Algorithm complexity matters for scalability
3. **Code Review Importance**: Multiple eyes catch more bugs
4. **Automated Testing**: Use tools to detect common vulnerabilities
5. **Defense in Depth**: Implement multiple layers of security controls

## Tools for Bug Detection

- **Static Analysis**: Bandit (Python), SonarQube, ESLint
- **Dynamic Testing**: OWASP ZAP, Burp Suite
- **Performance**: Python Profiler, load testing tools
- **Dependencies**: Safety, npm audit, Snyk

This project demonstrates the importance of thorough code review, security testing, and performance optimization in software development.