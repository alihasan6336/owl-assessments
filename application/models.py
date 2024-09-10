from application import db
from sqlalchemy import func
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Companies(db.Model, UserMixin):
    __tablename__ = 'companies'

    id                = db.Column(db.Integer(), primary_key=True)
    first_name        = db.Column(db.String(35), nullable=False)
    last_name         = db.Column(db.String(35))
    work_email        = db.Column(db.String(62), nullable=False, unique=True)
    department        = db.Column(db.String(50))
    phone_number      = db.Column(db.String(15), nullable=False, unique=True)
    country_code      = db.Column(db.String(6), nullable=False) # Max in counryCodes is 6. Noted.
    gender            = db.Column(db.String(1))
    date_of_birth     = db.Column(db.Date())
    company_name      = db.Column(db.String(100), nullable=False)
    country           = db.Column(db.String(60))
    state             = db.Column(db.String(50))
    city              = db.Column(db.String(50))
    postal_code       = db.Column(db.String(32))
    street_address    = db.Column(db.String(100))
    building          = db.Column(db.String(10))
    floor             = db.Column(db.String(10))
    apartment         = db.Column(db.String(10))
    address_2         = db.Column(db.String(255)) # Maxed at 100 in the validation. Noted.
    passhash          = db.Column(db.String(255))
    registration_date = db.Column(db.DateTime, default=func.now()) # Defalte timezone?
    active            = db.Column(db.Boolean, default=True)

    @property
    def is_active(self):
        return self.active

    def check_password(self, password):
        return check_password_hash(self.passhash, password)
