from flask import Flask
from auth import auth

app = Flask(__name__)  # initializing flask app

# register blueprint
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)