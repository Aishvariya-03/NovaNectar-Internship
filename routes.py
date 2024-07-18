from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import app
from app.models import User

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['username']
        # Replace with your authentication logic
        if user_id == 'admin' and request.form['password'] == 'admin_password':
            user = User(user_id)
            user.role = 'admin'
            login_user(user)
            return redirect(url_for('dashboard'))
        elif user_id == 'user' and request.form['password'] == 'user_password':
            user = User(user_id)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

# Protected route (dashboard)
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin():
        # Admin dashboard logic
        return render_template('dashboard.html', role='Admin', username=current_user.id)
    else:
        # User dashboard logic
        return render_template('dashboard.html', role='User', username=current_user.id)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
