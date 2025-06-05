from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    dish = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)


# Создаем таблицы при запуске
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        new_order = Order(
            customer_name=request.form['name'],
            dish=request.form['dish'],
            address=request.form['address']
        )
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)