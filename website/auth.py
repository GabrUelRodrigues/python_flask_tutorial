from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
	if request.method == "POST":
		email = request.form.get("email")
		name = request.form.get("name")
		password1 = request.form.get("password1")
		password2 = request.form.get("password2")

		user = User.query.filter_by(email=email).first()

		if user:
			flash("Email already registered.", category="error")

		elif len(email) <= 4:
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
			login_user(user, remember=True)
			flash("Account created!", category="success")
			
			return redirect(url_for("views.home"))

	return render_template("sign_up.html", user=current_user)

@auth.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		email = request.form.get("email")
		password = request.form.get("password")

		user = User.query.filter_by(email=email).first()

		if user:
			if check_password_hash(user.password, password):
				login_user(user, remember=True)
				flash("Logged in successfully!", category="success")
				return redirect(url_for("views.home"))
			
			else:
				flash("Incorrect password.", category="error")
		
		else:
			flash("User does not exist.", category="error")

	return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for("auth.login"))