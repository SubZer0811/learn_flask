from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField

class generate_rand_int(FlaskForm):
	a = IntegerField(label="Lower Limit")
	b = IntegerField(label="Upper Limit")
	submit = SubmitField(label="Generate")