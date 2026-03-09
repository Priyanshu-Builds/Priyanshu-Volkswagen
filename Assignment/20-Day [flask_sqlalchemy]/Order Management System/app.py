from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Priyanshu',
    'database': 'order_management'
}

def get_db():
    return mysql.connector.connect(**db_config)

def init_db():
    conn = mysql.connector.connect(host='localhost', user='root', password='Priyanshu')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS order_management")
    cursor.close()
    conn.close()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Order` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            quantity INT NOT NULL,
            price FLOAT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT *, (price * quantity) AS revenue FROM `Order`")
    orders = cursor.fetchall()
    total_revenue = sum(order['revenue'] for order in orders)
    cursor.close()
    conn.close()
    return render_template('index.html', orders=orders, total_revenue=total_revenue)

@app.route('/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `Order` (product_name, quantity, price) VALUES (%s, %s, %s)",
                       (product_name, quantity, price))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_order.html')

@app.route('/high_revenue')
def high_revenue():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT *, (price * quantity) AS revenue FROM `Order` WHERE (price * quantity) > 2000")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('high_revenue.html', orders=orders)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
