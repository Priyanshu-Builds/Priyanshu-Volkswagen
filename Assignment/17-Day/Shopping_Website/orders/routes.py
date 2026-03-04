from flask import Blueprint, render_template, request
import json

orders_bp = Blueprint("orders", __name__)

PRODUCT_IMAGES = {
    "laptop": "💻",
    "mouse": "🖱️",
    "keyboard": "⌨️",
    "headphones": "🎧",
    "monitor": "🖥️",
}


@orders_bp.route("/orders")
def view_orders():
    orders_cookie = request.cookies.get("orders")
    order_list = []
    if orders_cookie:
        try:
            order_list = json.loads(orders_cookie)
        except json.JSONDecodeError:
            order_list = []

        for order in order_list:
            for item in order["items"]:
                item["image"] = PRODUCT_IMAGES.get(item["name"], "📦")

    return render_template("orders.html", orders=order_list)
