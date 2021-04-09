from flask_wtf import Form
from wtforms import StringField

class RegistrationForm(Form):
    email = StringField('Email')
