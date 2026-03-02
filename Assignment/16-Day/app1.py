from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return jsonify({
        "number1": num1,
        "number2": num2,
        "addition": result
    })

if __name__ == "__main__":
    app.run(debug=True)