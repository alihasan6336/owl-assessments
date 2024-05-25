from application import db
from sqlalchemy import func


class Companies(db.Model):
    # __tablename__ = 'companies' # Is this necessary?

    # Column() or db.Column()? for all.

    id                = db.Column(db.Integer(), primary_key=True) # Autoincrement works?, How to make it unsigned?
    first_name        = db.Column(db.String(35), nullable=False)
    last_name         = db.Column(db.String(35))
    work_email        = db.Column(db.String(62), nullable=False) # Unique?
    department        = db.Column(db.String(50)) # Correct the length? Noted.
    phone_number      = db.Column(db.String(15), nullable=False, unique=True)
    country_code      = db.Column(db.String(5), nullable=False)
    gender            = db.Column(db.String(1))
    date_of_birth     = db.Column(db.Date())
    company_name      = db.Column(db.String(100), nullable=False) # Correct the length? Noted.
    country           = db.Column(db.String(60)) # Longest is 57 with spaces and a period. Noted.
    state             = db.Column(db.String(50)) # Longest is 49 with spaces and a period. Noted.
    city              = db.Column(db.String(35)) # Correct the length!!!
    postal_code       = db.Column(db.String(32)) # Longest is 32 but 16 is good. Noted.
    street_address    = db.Column(db.String(100)) # Longest is 95. Noted.
    building          = db.Column(db.String(10)) # Correct the length!!!
    floor             = db.Column(db.String(10))# Correct the length!!!
    apartment         = db.Column(db.String(10)) # Correct the length!!!
    address_2         = db.Column(db.Text) # Maxed at 100 in the validation. Noted.
    passhash          = db.Column(db.Text) # Correct the length based on the hash algorithm used.
    registration_date = db.Column(db.DateTime, default=func.now()) # Defalte timezone?


    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'first_name': self.first_name,
    #         'last_name': self.last_name,
    #         'work_email': self.work_email,
    #         'department': self.department,
    #         'phone_number': self.phone_number,
    #         'country_code': self.country_code,
    #         'gender': self.gender,
    #         'date_of_birth': self.date_of_birth,
    #         'company_name': self.company_name,
    #         'country': self.country,
    #         'state': self.state,
    #         'city': self.city,
    #         'postal_code': self.postal_code,
    #         'street_address': self.street_address,
    #         'building': self.building,
    #         'floor': self.floor,
    #         'apartment': self.apartment,
    #         'address_2': self.address_2,
    #         'passhash': self.passhash,
    #         'registration_date': self.registration_date
    #     }
        
