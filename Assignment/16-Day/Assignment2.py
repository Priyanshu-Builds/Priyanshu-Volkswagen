from flask import Flask, render_template, request

app = Flask(__name__)

employees = [
    {"name": "Priyanshu", "department": "SDE", "salary": 60000},
    {"name": "Ayush", "department": "HR", "salary": 50000},
    {"name": "Aryan", "department": "IT", "salary": 70000},
]

@app.route("/dashboard")
def dashboard():
    role = request.args.get("role", "employee").lower()

    return render_template(
        "dashboard.html",
        role=role,
        employees=employees
    )

if __name__ == "__main__":
    app.run(debug=True)