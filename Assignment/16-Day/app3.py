from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo")
def demo():
    return render_template("2.html", name="arun")

if __name__ == "__main__":
    app.run(debug=True)