from flask import Flask, render_template

app = Flask(__name__)

@app.route("/demo")
def show_names():
    names = ["arun", "amit", "priya"]

    upper_names = [name.upper() for name in names]

    return render_template("1.html", names=upper_names)

if __name__ == "__main__":
    app.run(debug=True)