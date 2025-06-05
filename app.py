import os
from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from urllib.parse import urlparse
app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'static'))

DATABASE_URL = os.environ.get('DATABASE_URL')
result = urlparse(DATABASE_URL)

conn = psycopg2.connect(
    database=result.path[1:],
    user=result.username,
    password=result.password,
    host=result.hostname,
    port=result.port
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        # Временное решение без БД
        print(f"New order: {request.form['name']}, {request.form['dish']}")
        return redirect(url_for('home'))
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)