from flask_wtf import Form
from wtforms import StringField, BooleanField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Regexp,EqualTo
from .models import User

# class LoginForm(Form):
#     openid = StringField('openid', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)
class LoginForm(Form):
	nickname = StringField('Nickname', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')

class CommentForm(Form):
	comment = StringField('comment', validators=[DataRequired()])

class RegistrationForm(Form):
	nickname=StringField('Nickname',validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('Confirm password', validators=[DataRequired()])
	submit = SubmitField('Register')


	def validate_nickname(self, field):
		if User.query.filter_by(nickname=field.data).first():
			raise ValidationError('Nickname already registered.')
		