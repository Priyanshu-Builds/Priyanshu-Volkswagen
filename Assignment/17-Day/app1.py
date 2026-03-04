from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    message = ""

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            message = "Fields should not be blank"

        elif "@" not in email:
            message = "Email should have @ symbol"

        elif len(password) < 5 or len(password) > 8:
            message = "Password should be at least 5 characters and maximum 8 characters"

        else:
            message = "Form submitted successfully!"

    return render_template("form.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)