from flask import Flask, render_template

app = Flask(__name__)

comments = [
    {
        "username": "John",
        "comment": "This product is good",
        "likes": 120,
        "flagged": False
    },
    {
        "username": "Ayush",
        "comment": "  This product is dumb and stupid  ",
        "likes": 45,
        "flagged": True
    },
    {
        "username": "Aryan",
        "comment": "Excellent service!" * 20,
        "likes": 250,
        "flagged": False
    }
]

@app.route("/comments")
def show_comments():

    bad_words = ["dumb", "stupid"]

    for c in comments:
        for word in bad_words:
            c["comment"] = c["comment"].replace(word, "***")

    total_comments = len(comments)
    total_flagged = len([c for c in comments if c["flagged"]])
    most_liked = max(comments, key=lambda x: x["likes"])

    usernames_joined = ", ".join([c["username"] for c in comments])

    return render_template(
        "comments.html",
        comments=comments,
        total_comments=total_comments,
        total_flagged=total_flagged,
        most_liked=most_liked,
        usernames_joined=usernames_joined
    )

if __name__ == "__main__":
    app.run(debug=True)