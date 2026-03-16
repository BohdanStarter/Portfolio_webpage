from flask import Flask, render_template, request, redirect, flash
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    requests.post(
        "https://api.mailgun.net/v3/sandbox976ed9dc149a49c48c73280d00e81f7b.mailgun.org/messages",
        auth=("api", os.getenv("API_KEY")),
        data={
            "from": f"{name} <postmaster@sandbox976ed9dc149a49c48c73280d00e81f7b.mailgun.org>",
            "to": "bogdan2cs2@gmail.com",
            "subject": "New message from website (Contact Me Form)",
            "text": f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
        }
    )
    
    return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/toMain", methods=["GET"])
def not_found_transition():
    print("Redirecting...")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)