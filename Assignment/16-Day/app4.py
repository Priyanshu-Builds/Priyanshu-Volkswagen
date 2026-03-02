from flask import Flask, render_template

app = Flask(__name__)

@app.route("/students")
def students():
    students = [
        {"name": "John", "marks": 80},
        {"name": "Amit", "marks": 70},
        {"name": "Riya", "marks": 40}
    ]
    
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)