from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Priyanshu',
    'database': 'library_management'
}

def get_db():
    return mysql.connector.connect(**db_config)

def init_db():
    conn = mysql.connector.connect(host='localhost', user='root', password='Priyanshu')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_management")
    cursor.close()
    conn.close()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Book (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            author VARCHAR(200) NOT NULL,
            copies INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        copies = int(request.form['copies'])
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Book (title, author, copies) VALUES (%s, %s, %s)",
                       (title, author, copies))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/borrow/<int:book_id>')
def borrow_book(book_id):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Book WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    if book and book['copies'] > 0:
        cursor.execute("UPDATE Book SET copies = copies - 1 WHERE id = %s", (book_id,))
        conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/unavailable')
def unavailable_books():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Book WHERE copies = 0")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('unavailable.html', books=books)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)