from flask_wtf import FlaskForm

from wtforms import StringField, RadioField, DecimalField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, ValidationError, Optional, Email

class CreateDelegateForm(FlaskForm):
	
	first_name = StringField('First Name', [Required()])
	last_name = StringField('Last Name', [Required()])
	email_address = EmailField('Email Address', [Required(), Email()])
	contact_number = StringField('Contact Number', [Required()])
	is_student = RadioField('Student or Professional', [Required()], choices=[('student', 'Student'), ('professional', 'Professional')])
	school_or_company = StringField('School/Company', [Required()])
	course_or_position = StringField('Course/Position', [Required()])

	# def validate_first_name(form, field):
	# 	if field.data :
	# 		raise ValidationError("Enter a valid name")

	# def validate_last_name(form, field):
	# 	if field.data :
	# 		raise ValidationError("Enter a valid name")

	# def validate_contact_number(form, field): 
	# 	if field.data :
	# 		raise ValidationError("Enter a valid contact number")

