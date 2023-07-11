from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
	if request.method == "POST":
		email = request.form.get("email")
		name = request.form.get("name")
		password1 = request.form.get("password1")
		password2 = request.form.get("password2")

		if len(email) <= 4:
			flash("Email must be at least 4 characters.", category="error")

		elif len(name) <= 1:
			flash("Name must be at least 2 characters.", category="error")

		elif len(password1) < 8:
			flash("Password must be at least 8 characters.", category="error")

		elif password1 != password2:
			flash("Passwords don't match.", category="error")

		else:
			new_user = User(email=email, name=name, password=generate_password_hash(password1, method="scrypt"))
			db.session.add(new_user)
			db.session.commit()
			flash("Account created!", category="success")
			
			return redirect(url_for("views.home"))

	return render_template("sign_up.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
	return render_template("login.html")

@auth.route("/logout")
def logout():
	return "<h1>Logout</h1>"