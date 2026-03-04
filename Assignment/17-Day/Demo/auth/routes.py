from flask import render_template, request
from auth import auth
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@auth.route('/login', methods=["GET","POST"])
def login():

    if request.method == "POST":

        name = request.form.get("name")
        password = request.form.get("password")

        file = request.files.get("myfile")

        if file and file.filename != "":
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            return f"File uploaded successfully. Welcome {name}"

        return "No file selected"

    return render_template("auth/index.html")