from application import app
from flask import render_template

@app.route("/")
def test():
    return "Helthy"

@app.route("/login")
def login():
    return render_template("login-test.html")

@app.route("/register"  )
def register():
    return render_template("register-test.html")