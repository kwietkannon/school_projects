''' Jamie Garcia CYOP 300 Section 6381 Project 6'''

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """The home page of the website."""
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)

@app.route('/about')
def about():
    """The about page of the website."""
    return render_template('about.html')

@app.route('/peppers')
def contact():
    """The contact page of the website."""
    return render_template('peppers.html')

# if __name__ == '__main__':
#     app.run(debug=True)
