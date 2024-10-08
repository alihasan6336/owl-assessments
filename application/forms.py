from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, DateField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp
from application.form_custom_validator import NumericFieldValidator, UniqueFieldValidator
from datetime import date
from application.data_lists import counryCodes

# Define constants for the password validation
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!*?])[A-Za-z\d@#$%^&+=!*?]{8,20}$'
PASSWORD_MESSAGE = 'Password must be 8-20 characters long and include at least one lowercase letter, one uppercase letter, one digit, and one special character (@#$%^&+=!*?).'

class RegisterForm(FlaskForm):
    first_name       = StringField('First Name', validators=[DataRequired(), Length(min=2, max=35)])
    last_name        = StringField('Last Name', validators=[Length(max=35)])
    work_email       = EmailField('Work Email', validators=[DataRequired(), Email(), Length(max=62), UniqueFieldValidator("Work Email already exists.")])
    department       = StringField('Department', validators=[Length(max=50)])
    phone_number     = StringField('Phone Number', validators=[DataRequired(), Length(max=15), NumericFieldValidator("Phone Number must contain only numbers."), UniqueFieldValidator("Phone number already exists.")])
    country_code     = SelectField('Code +', validators=[DataRequired(), Length(max=6)], choices=counryCodes)
    gender           = StringField("Gender", validators=[Length(max=1)]) # Do it.
    date_of_birth    = DateField('Date of Birth', format='%Y-%m-%d', validators=[Optional()])
    company_name     = StringField('Company Name', validators=[DataRequired(), Length(max=100)])
    country          = StringField('Country', validators=[Length(max=60)])
    state            = StringField('State', validators=[Length(max=50)])
    city             = StringField('City', validators=[Length(max=50)])
    postal_code      = StringField('Postal Code', validators=[Length(max=32), NumericFieldValidator("Postal code must contain only numbers.")])
    street_address   = StringField('Street Address', validators=[Length(max=100)])
    building         = StringField('Building', validators=[Length(max=10)])
    floor            = StringField('Floor', validators=[Length(max=10)])
    apartment        = StringField('Apartment', validators=[Length(max=10)])
    address_2        = StringField('Address 2', validators=[Length(max=100)])
    password         = PasswordField('Password', validators=[DataRequired(), Regexp(PASSWORD_REGEX, message=PASSWORD_MESSAGE,)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', 'Passwords must match.')])
    submit           = SubmitField('Register') 


class LoginForm(FlaskForm):
    work_email    = StringField('Work Email', validators=[DataRequired(), Email(), Length(max=62)])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me') # add it?
    submit   = SubmitField('Login')