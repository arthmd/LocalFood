import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'static'))



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