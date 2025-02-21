''' Jamie Garcia CYOP 300 Section 6381 Project 6'''

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, session
import re

app = Flask(__name__)
app.secret_key = 'mysecretkey'

users = {
    'user': {
        'username': 'jamie',
        'password': 'password'
    }
}

@app.route('/')
def homepage():
    """The home page of the website."""
    current_time = datetime.now()
    return render_template('homepage.html', current_time=current_time)

@app.route('/about/')
def about():
    """The about page of the website."""
    return render_template('about.html')

@app.route('/peppers/')
def peppers():
    """The contact page of the website."""
    return render_template('peppers.html')

@app.route('/register/',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(password) < 12 or not any(char.isupper() for char \
        in password) or not any(char.islower() for char in password) \
        or not any(char.isdigit() for char in password) or not any(char in '!@#$%^&*()' for char in password):

            return render_template('register.html', error='Password must be at least 12 characters long and include at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character.')

        users[username] = {'username': username, 'password': password}
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    """The user login page."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and the password is correct
        if username in users and users[username]['password'] == password:
            session['user'] = username
            return redirect(url_for('protected'))
        else:
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')

@app.route('/protected/')
def protected():
    """A protected page that can only be accessed after login."""
    if 'user' in session:
        return render_template('protected.html', user=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    """Logs out the user and redirects to the homepage."""
    session.pop('user', None)
    return redirect(url_format('homepage'))


