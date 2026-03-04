from flask import Flask

app = Flask(__name__)
app.secret_key = "mini_shop_secret_key"

from products.routes import products_bp
from cart.routes import cart_bp
from orders.routes import orders_bp

app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(orders_bp)

if __name__ == "__main__":
    app.run(debug=True)
