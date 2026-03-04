from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")

        visit_count = request.cookies.get("visit_count")

        if visit_count:
            visit_count = int(visit_count) + 1
        else:
            visit_count = 1

        response = make_response(
            f"Hello {name}, You visited this page {visit_count} times"
        )

        response.set_cookie("visit_count", str(visit_count), max_age=60*60*24)

        return response

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)