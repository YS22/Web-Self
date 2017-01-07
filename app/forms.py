 # -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, BooleanField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Regexp,EqualTo
from .models import User

# class LoginForm(Form):
#     openid = StringField('openid', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)
class LoginForm(Form):
	nickname = StringField(u'用户名:', validators=[DataRequired()])
	password = PasswordField(u'密码:', validators=[DataRequired()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField(u'登录')

class CommentForm(Form):
	comment = StringField('comment', validators=[DataRequired()])

class RegistrationForm(Form):
	nickname=StringField(u'用户名:',validators=[DataRequired()])
	password = PasswordField(u'密码:', validators=[DataRequired(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField(u'重复密码:', validators=[DataRequired()])
	submit = SubmitField(u'注册')


	def validate_nickname(self, field):
		if User.query.filter_by(nickname=field.data).first():
			raise ValidationError('Nickname already registered.')
		
