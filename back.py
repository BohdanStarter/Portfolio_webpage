from flask import Flask, render_template, request, redirect, flash
import requests
import os
from dotenv import load_dotenv
from email_validator import validate_email, EmailNotValidError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman

load_dotenv()

app = Flask(__name__)

Talisman(app, content_security_policy=None)

app.secret_key = os.getenv("SECRET_KEY")

limiter = Limiter(get_remote_address, app=app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
@limiter.limit("5 per minute")
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    name = name.replace("\n", "").replace("\r", "").strip()

    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError:
        return "Invalid email", 400

    if len(message) > 2000:
        return "Message too long", 400

    try:
        response = requests.post(
            "https://api.mailgun.net/v3/sandbox976ed9dc149a49c48c73280d00e81f7b.mailgun.org/messages",
            auth=("api", os.getenv("API_KEY")),
            data={
                "from": f"{name} <postmaster@sandbox976ed9dc149a49c48c73280d00e81f7b.mailgun.org>",
                "to": "bogdan2cs2@gmail.com",
                "subject": "New message from website (Contact Me Form)",
                "text": f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            },
            timeout=10,
        )

        if response.status_code != 200:
            return "Email service error", 500

    except requests.exceptions.RequestException:
        return "Email service unavailable", 500

    flash("Message sent successfully!")
    return redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/toMain", methods=["GET"])
def not_found_transition():
    print("Redirecting...")
    return redirect("/")


if __name__ == "__main__":
    app.run()
