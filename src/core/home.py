from flask import Blueprint, flash, redirect, render_template, request

from core.models import Delegates
from core.forms import CreateDelegateForm
from core import config

app = Blueprint("home", __name__)

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("create.html")

@app.route("/register", methods=["GET"])
def register():
	form = CreateDelegateForm()
	return render_template("create.html", form=form)

@app.route("/register", methods=["POST"])
def create():
	form = CreateDelegateForm()
	if form.validate_on_submit():
		# print(request.form)
		if request.form.get('is_student')=="student":
			is_student = True
		else:
			is_student = False
		Delegates.create(
			first_name=request.form.get('first_name'),
			last_name=request.form.get('last_name'),
			email_address=request.form.get('email_address'),
			contact_number=request.form.get('contact_number'),
			is_student=is_student,
			school_or_company=request.form.get('school_or_company'),
			course_or_position=request.form.get('course_or_position')
		)
		flash("Success!!")
		return redirect('/register')
	return render_template("create.html", form=form)