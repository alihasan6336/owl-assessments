from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, DateField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional
from application.form_custom_validator import NumericValidator
from datetime import date

class RegisterForm(FlaskForm):
    first_name       = StringField('First Name', validators=[DataRequired(), Length(min=2, max=35)])
    last_name        = StringField('Last Name', validators=[Length(max=35)])
    work_email       = EmailField('Work Email', validators=[DataRequired(), Email(), Length(max=62)])
    department       = StringField('Department', validators=[Length(max=50)])
    phone_number     = StringField('Phone Number', validators=[DataRequired(), Length(max=15), NumericValidator("Phone number")])
    country_code     = StringField('Code +', validators=[DataRequired(), Length(max=5)])
    gender           = StringField("Gender", validators=[Length(max=1)]) # Do it. 
    date_of_birth    = DateField('Date of Birth',validators=[Optional()]) # Correct the format!!!
    company_name     = StringField('Company Name', validators=[DataRequired(), Length(max=100)])
    country          = StringField('Country', validators=[Length(max=60)])
    state            = StringField('State', validators=[Length(max=50)])
    city             = StringField('City', validators=[Length(max=35)])
    postal_code      = StringField('Postal Code', validators=[Length(max=32), NumericValidator("Postal code")])
    street_address   = StringField('Street Address', validators=[Length(max=100)])
    building         = StringField('Building', validators=[Length(max=10)])
    floor            = StringField('Floor', validators=[Length(max=10)])
    apartment        = StringField('Apartment', validators=[Length(max=10)])
    address_2        = StringField('Address 2', validators=[Length(max=100)]) # Correct the length!!!
    password         = PasswordField('Password', validators=[DataRequired()]) # Password validations!!!
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', 'Passwords must match.')]) # EqualTo() 'Password' or 'password'?
    submit           = SubmitField('Register') 


class LoginForm(FlaskForm):
    email    = StringField('Email', validators=[DataRequired(), Email(), Length(max=62)])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember = BooleanField('Remember Me') # add it?
    submit   = SubmitField('Login')