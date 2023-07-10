from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
	return render_template("sign_up.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
	return render_template("login.html")

@auth.route("/logout")
def logout():
	return "<h1>Logout</h1>"