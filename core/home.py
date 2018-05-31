from flask import Blueprint, flash, redirect, render_template, request
from markupsafe import escape

from core.models import Delegates
from core.forms import CreateDelegateForm
from core import config

app = Blueprint("home", __name__)

@app.route("/register", methods=["GET"])
def index():
	return redirect('/')
	# return render_template('index.html')

@app.route("/", methods=["GET"])
def register():
	form = CreateDelegateForm()
	return render_template("create.html", form=form)

@app.route("/", methods=["POST"])
def create():
	form = CreateDelegateForm()
	if form.validate_on_submit():
		# print(request.form)
		if request.form.get('is_student')=="student":
			is_student = True
		else:
			is_student = False
		Delegates.create(
			first_name=escape(request.form.get('first_name')),
			last_name=escape(request.form.get('last_name')),
			email_address=escape(request.form.get('email_address')),
			contact_number=escape(request.form.get('contact_number')),
			is_student=is_student,
			school_or_company=escape(request.form.get('school_or_company')),
			course_or_position=escape(request.form.get('course_or_position'))
		)
		flash("Success!!")
		return render_template('success.html')
	return render_template('create.html', form=form)

@app.route("/list", methods=["GET"])
def list():
	return render_template('list.html', delegates=[row for row in Delegates.select().dicts()])

@app.route("/disintegrate", methods=["GET"])
def disintegrate():
	Delegates.drop_table()
	return redirect('/')

@app.route("/flush", methods=["GET"])
def flush():
	Delegates.delete()
	return redirect('/')