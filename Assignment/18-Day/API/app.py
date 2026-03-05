from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = []

@app.route("/")
def home():
    return "Flask API Running"

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json

    products.append(data)

    return jsonify({
        "message": "Product added successfully",
        "data": data
    })


if __name__ == "__main__":
    app.run(debug=True)