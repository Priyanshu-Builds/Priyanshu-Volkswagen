from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Priyanshu",
        database="event_db"
    )

@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    name = data.get("name")
    total_seats = data.get("total_seats")

    if not name or total_seats is None:
        return jsonify({"error": "name and total_seats are required"}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO events (name, total_seats, available_seats) VALUES (%s, %s, %s)",
        (name, total_seats, total_seats)
    )
    db.commit()
    event_id = cursor.lastrowid
    cursor.close()
    db.close()

    return jsonify({
        "message": "Event created successfully",
        "event": {
            "id": event_id,
            "name": name,
            "total_seats": total_seats,
            "available_seats": total_seats
        }
    }), 201


@app.route("/events", methods=["GET"])
def list_events():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(events), 200


@app.route("/events/full", methods=["GET"])
def full_events():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events WHERE available_seats = 0")
    events = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(events), 200


@app.route("/register/<int:event_id>", methods=["POST"])
def register(event_id):
    data = request.get_json()
    user_name = data.get("user_name")

    if not user_name:
        return jsonify({"error": "user_name is required"}), 400

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
    event = cursor.fetchone()

    if not event:
        cursor.close()
        db.close()
        return jsonify({"error": "Event not found"}), 404

    if event["available_seats"] == 0:
        cursor.close()
        db.close()
        return jsonify({"error": "No seats available. Registration failed."}), 400
    cursor.execute(
        "INSERT INTO registrations (user_name, event_id) VALUES (%s, %s)",
        (user_name, event_id)
    )
    cursor.execute(
        "UPDATE events SET available_seats = available_seats - 1 WHERE id = %s",
        (event_id,)
    )
    db.commit()
    registration_id = cursor.lastrowid
    cursor.close()
    db.close()

    return jsonify({
        "message": "Registration successful",
        "registration": {
            "id": registration_id,
            "user_name": user_name,
            "event_id": event_id
        }
    }), 201


if __name__ == "__main__":
    app.run(debug=True)