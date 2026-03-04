from flask import Blueprint, render_template, request, redirect, url_for, make_response
import json

products_bp = Blueprint("products", __name__)

PRODUCTS = [
    {"name": "Laptop", "price": 54999, "image": "💻", "description": "High-performance laptop with 16GB RAM"},
    {"name": "Mouse", "price": 799, "image": "🖱️", "description": "Ergonomic wireless mouse"},
    {"name": "Keyboard", "price": 2499, "image": "⌨️", "description": "Mechanical RGB keyboard"},
    {"name": "Headphones", "price": 4999, "image": "🎧", "description": "Noise-cancelling over-ear headphones"},
    {"name": "Monitor", "price": 18999, "image": "🖥️", "description": "27-inch 4K Ultra HD display"},
]


@products_bp.route("/")
def index():
    return render_template("products.html", products=PRODUCTS)


@products_bp.route("/add/<product_name>", methods=["POST"])
def add_to_cart(product_name):
    cart = {}
    cart_cookie = request.cookies.get("cart")
    if cart_cookie:
        try:
            cart = json.loads(cart_cookie)
        except json.JSONDecodeError:
            cart = {}

    product_key = product_name.lower()
    cart[product_key] = cart.get(product_key, 0) + 1

    response = make_response(redirect(url_for("products.index")))
    response.set_cookie("cart", json.dumps(cart), max_age=60 * 60 * 24 * 7)
    return response
