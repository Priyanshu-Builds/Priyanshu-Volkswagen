from flask import Blueprint, render_template, request, redirect, url_for, make_response
import json

cart_bp = Blueprint("cart", __name__)

PRODUCT_PRICES = {
    "laptop": 54999,
    "mouse": 799,
    "keyboard": 2499,
    "headphones": 4999,
    "monitor": 18999,
}

PRODUCT_IMAGES = {
    "laptop": "💻",
    "mouse": "🖱️",
    "keyboard": "⌨️",
    "headphones": "🎧",
    "monitor": "🖥️",
}


@cart_bp.route("/cart")
def view_cart():
    cart_cookie = request.cookies.get("cart")
    cart_items = []
    total = 0
    item_count = 0

    if cart_cookie:
        try:
            cart = json.loads(cart_cookie)
        except json.JSONDecodeError:
            cart = {}

        for product_name, quantity in cart.items():
            price = PRODUCT_PRICES.get(product_name, 0)
            subtotal = price * quantity
            total += subtotal
            item_count += quantity
            cart_items.append({
                "name": product_name,
                "price": price,
                "quantity": quantity,
                "subtotal": round(subtotal, 2),
                "image": PRODUCT_IMAGES.get(product_name, "📦"),
            })

    return render_template("cart.html", cart_items=cart_items, total=round(total, 2), item_count=item_count)


@cart_bp.route("/cart/update", methods=["POST"])
def update_cart():
    product_name = request.form.get("product_name")
    action = request.form.get("action")

    cart_cookie = request.cookies.get("cart")
    cart = {}
    if cart_cookie:
        try:
            cart = json.loads(cart_cookie)
        except json.JSONDecodeError:
            cart = {}

    if product_name in cart:
        if action == "increase":
            cart[product_name] += 1
        elif action == "decrease":
            cart[product_name] -= 1
            if cart[product_name] <= 0:
                del cart[product_name]

    response = make_response(redirect(url_for("cart.view_cart")))
    response.set_cookie("cart", json.dumps(cart), max_age=60 * 60 * 24 * 7)
    return response


@cart_bp.route("/cart/clear", methods=["POST"])
def clear_cart():
    response = make_response(redirect(url_for("cart.view_cart")))
    response.delete_cookie("cart")
    return response


@cart_bp.route("/cart/place-order", methods=["POST"])
def place_order():
    cart_cookie = request.cookies.get("cart")
    if not cart_cookie:
        return redirect(url_for("cart.view_cart"))

    try:
        cart = json.loads(cart_cookie)
    except json.JSONDecodeError:
        return redirect(url_for("cart.view_cart"))

    if not cart:
        return redirect(url_for("cart.view_cart"))

    orders_cookie = request.cookies.get("orders")
    orders = []
    if orders_cookie:
        try:
            orders = json.loads(orders_cookie)
        except json.JSONDecodeError:
            orders = []

    total = 0
    items = []
    for product_name, quantity in cart.items():
        price = PRODUCT_PRICES.get(product_name, 0)
        subtotal = price * quantity
        total += subtotal
        items.append({"name": product_name, "quantity": quantity, "price": price})

    order = {
        "id": len(orders) + 1,
        "items": items,
        "total": round(total, 2),
    }
    orders.append(order)

    response = make_response(redirect(url_for("orders.view_orders")))
    response.set_cookie("orders", json.dumps(orders), max_age=60 * 60 * 24 * 30)
    response.delete_cookie("cart")
    return response
