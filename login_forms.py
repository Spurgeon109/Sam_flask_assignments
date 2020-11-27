from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class SignUpForms(FlaskForm):
    FirstName = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    LastName = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    CPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    SignUp = SubmitField('SignUp')

class SignInForms(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    SignIn = SubmitField('SignIn')
