from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, DateField, PasswordField, SubmitField, SelectField, BooleanField, TextAreaField, DateTimeField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp, NumberRange
from application.form_custom_validator import NumericFieldValidator, UniqueFieldValidator, ExpiryDateValidator
from datetime import date
from application.data_lists import counryCodes, test_types_ls, question_types

# Define constants for the password validation
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!*?])[A-Za-z\d@#$%^&+=!*?]{8,30}$'
PASSWORD_MESSAGE = 'Password must be 8-20 characters long and include at least one lowercase letter, one uppercase letter, one digit, and one special character (@#$%^&+=!*?).'

class RegisterForm(FlaskForm):
    first_name       = StringField('First Name', validators=[DataRequired(), Length(min=2, max=35)])
    last_name        = StringField('Last Name', validators=[Length(max=35)])
    work_email       = EmailField('Work Email', validators=[DataRequired(), Email(), Length(max=62), UniqueFieldValidator("Work Email already exists.")])
    department       = StringField('Department', validators=[Length(max=50)])
    phone_number     = StringField('Phone Number', validators=[DataRequired(), Length(max=15), NumericFieldValidator("Phone Number must contain only numbers."), UniqueFieldValidator("Phone number already exists.")])
    country_code     = SelectField('Code +', validators=[DataRequired(), Length(max=6)], choices=counryCodes)
    gender           = StringField("Gender", validators=[Length(max=1)]) # Do it.
    date_of_birth    = DateField('Date of Birth', format='%Y-%m-%d', validators=[Optional()]) # Validate the date
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
    password = PasswordField('Password', validators=[DataRequired(), Length(max=30)])
    # remember = BooleanField('Remember Me') # add it?
    submit   = SubmitField('Login')


class TestForm(FlaskForm):

    title = StringField('Test Title', validators=[DataRequired(), Length(max=100)])
    duration = IntegerField('Duration (minutes)', validators=[NumberRange(min=1, max=600)], default=60)
    description = TextAreaField('Description', validators=[Length(max=255)])
    instructions = TextAreaField('Instructions', validators=[Length(max=255)])
    ctype = SelectField('Test type', choices=test_types_ls, validators=[Length(max=100)])
    other_type = StringField('Specify your type:', validators=[Length(max=100)])
    num_of_questions = IntegerField('Number of Questions', validators=[DataRequired(), NumberRange(min=1, max=100)])
    total_marks = IntegerField('Total Marks', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    expiry_date = DateTimeField('Expiry Date', format='%Y-%m-%d %H:%M:%S', validators=[Optional(), ExpiryDateValidator()], render_kw={"placeholder": "YYYY-MM-DD HH:MM:SS"})
    multiple_sections = BooleanField('Do you want to have more than one section in the test?')
    one_section_per_page = BooleanField('Do you want to present every section in one page?')
    correction_type = SelectField('Correction Type', choices=[('a', 'Automatic'), ('m', 'Manual'), ('c', 'Custom')], validators=[DataRequired()])
    submit = SubmitField('Create Test')


class QuestionForm(FlaskForm):
    question = TextAreaField('Question', validators=[DataRequired(), Length(max=255)])
    type = SelectField('Question Type', choices=question_types, validators=[DataRequired()])
    marks = IntegerField('Marks', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    submit = SubmitField('Add Question')


class OptionForm(FlaskForm):
    option = TextAreaField('Option 1', validators=[Length(max=255)]) #add required
    is_correct = SelectField('Is Correct', choices=[('y', 'Yes'), ('n', 'No')]) # can this be changed by the user? needs DataRequired?
    submit = SubmitField('Add Option')