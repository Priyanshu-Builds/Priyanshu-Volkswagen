from flask import Flask, render_template, request

app = Flask(__name__)

cars_data = [
    {"name": "Polo", "brand": "Volkswagen", "price": 800000, "available": True},
    {"name": "Virtus", "brand": "Volkswagen", "price": 1200000, "available": True},
    {"name": "Octavia", "brand": "Skoda", "price": 2500000, "available": False},
    {"name": "Audi A4", "brand": "Audi", "price": 4500000, "available": True},
    {"name": "Lamborghini Urus", "brand": "Lamborghini", "price": 30000000, "available": False},
]

@app.route("/products")
def products():
    filtered_cars = cars_data.copy()

    brand = request.args.get("brand")
    availability = request.args.get("available")
    sort_order = request.args.get("sort")

    if brand:
        filtered_cars = [
            car for car in filtered_cars
            if car["brand"].lower() == brand.lower()
        ]

    if availability:
        is_available = availability.lower() == "true"
        filtered_cars = [
            car for car in filtered_cars
            if car["available"] == is_available
        ]

    if sort_order == "low":
        filtered_cars.sort(key=lambda x: x["price"])
    elif sort_order == "high":
        filtered_cars.sort(key=lambda x: x["price"], reverse=True)

    total = len(filtered_cars)

    return render_template("products.html", cars=filtered_cars, total=total)

if __name__ == "__main__":
    app.run(debug=True)