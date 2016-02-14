from flask.ext.wtf import Form
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email


class LoginForm(Form):
    email_field = EmailField("Email", validators=[InputRequired("Please enter an email."), Email("That is not a valid email, dummy!")])

    password_field = PasswordField("Password", validators=[InputRequired("Please enter a password.")])
