![Python](https://img.shields.io/badge/Python3.x-yellow)
![Flask](https://img.shields.io/badge/Flask-black)
![HTML5](https://img.shields.io/badge/HTML5-orange)
![CSS3](https://img.shields.io/badge/CSS3-blue)

# Personal Portfolio Website

A personal portfolio website built with **Python and Flask** that presents my projects, background, and provides a secure contact form that allows visitors to send messages directly to my email.

The project demonstrates practical backend development skills such as form handling, server-side validation, API integration, rate limiting, environment variable management, and basic web security practices.

---

# Live Purpose of the Project

The goal of this project is to create a simple but realistic full-stack web application that demonstrates how a backend server interacts with a frontend interface and external APIs.

The website allows visitors to:

* view information about me
* explore programming projects
* contact me through a form

When a user submits the contact form, the server validates the input and sends the message to my email using an external email service.

---

# Features

## Portfolio Website

The website contains several sections:

* **Home** – introduction and summary
* **About** – education and background
* **Projects** – overview of programming work
* **Contact** – form to send messages

The layout is responsive and adapts to different screen sizes.

---

## Contact Form Backend

The backend is implemented using Flask.

Form workflow:

1. A user fills out the contact form.
2. The browser sends a POST request to the `/send` route.
3. The server validates the submitted data.
4. The message is sent through the Mailgun API.
5. The user is redirected back to the homepage with a success message.

This demonstrates how a backend server processes form submissions and interacts with external services.

---

# Security and Backend Practices

Even though this is a small portfolio project, several important backend practices were implemented.

## Server-side Input Validation

Client-side validation in HTML can be bypassed, so all inputs are validated again on the server.

The server validates:

* email format
* message length
* form data integrity

Example:

```python
try:
    valid = validate_email(email)
    email = valid.email
except EmailNotValidError:
    return "Invalid email", 400
```

---

## Protection Against Email Header Injection

User input is sanitized before being used in email headers.

Newline characters are removed from the `name` field to prevent header injection attacks.

```python
name = name.replace("\n", "").replace("\r", "").strip()
```

---

## Rate Limiting

The contact endpoint is protected using request rate limiting.

Example limit:

```
5 requests per minute per IP address
```

This helps protect the form from spam or automated bots.

---

## Environment Variables

Sensitive credentials are stored outside the source code using environment variables.

Secrets include:

* Mailgun API key
* Flask secret key

Example `.env` file:

```
API_KEY=your_mailgun_api_key
SECRET_KEY=your_secret_key
```

The `.env` file is excluded from the repository using `.gitignore`.

---

## Error Handling

Network requests to the email service are wrapped in exception handling.
If the email service is unavailable, the application returns an appropriate error instead of crashing.

---

# Technologies Used

## Backend

* Python
* Flask
* Requests
* Flask-Limiter
* Email Validator
* Python Dotenv

## Frontend

* HTML5
* CSS3
* Responsive design

## External Service

* Mailgun API for email delivery

---

# Project Structure

```
project/
│
├── app.py
│
├── templates/
│   ├── index.html
│   └── 404.html
│
├── static/
│   ├── styles.css
│   └── images/
│
├── .env
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the repository

```
git clone https://github.com/BohdanStarter/Portfolio_webpage.git
cd portfolio-website
```

---

## 2. Create a virtual environment (recommended)

```
python -m venv venv
```

Activate the environment.

Linux / macOS:

```
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root.

```
API_KEY=your_mailgun_api_key
SECRET_KEY=your_secret_key
```

---

## 5. Run the application

```
python app.py
```

The server will start locally at:

```
http://127.0.0.1:5000
```

---

# What I Learned

While building this project I practiced:

* backend development with Flask
* handling form submissions in a web application
* integrating an external API (Mailgun email service)
* implementing server-side input validation
* protecting endpoints with rate limiting
* managing secrets using environment variables
* handling network errors safely

This project helped strengthen my understanding of how backend servers interact with user input and external services.

---

# Possible Future Improvements

Possible improvements include:

* CAPTCHA to prevent bots
* improved logging
* deployment with Gunicorn
* automated tests
* Docker containerization

---

# Author

Bohdan Bulakevych

GitHub:
https://github.com/BohdanStarter

LinkedIn:
https://www.linkedin.com/in/bohdan-bulakevych-5510b416b/

Portfolio:
https://portfolio-webpage-nlty.onrender.com/

---

# License

This project is created for educational and portfolio purposes.
