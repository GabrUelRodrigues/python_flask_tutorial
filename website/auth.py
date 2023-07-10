from flask import Blueprint, render_template, request, flash

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
			#Add user to the database
			flash("Account created!", category="success")

	return render_template("sign_up.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
	return render_template("login.html")

@auth.route("/logout")
def logout():
	return "<h1>Logout</h1>"