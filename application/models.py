from application import db
from sqlalchemy import func
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Company(db.Model, UserMixin):
    __tablename__ = 'companies'

    id                = db.Column(db.BigInteger(), primary_key=True)
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
    registration_date = db.Column(db.DateTime, default=datetime.utcnow) # Defalte timezone? works?
    active            = db.Column(db.Boolean, default=True)

    @property   
    def is_active(self):
        return self.active
    
    # @property
    # def is_authenticated(self):
    #     return True
    
    # @property
    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     return str(self.id)
    
    
    def check_password(self, password):
        return check_password_hash(self.passhash, password)
    

class Test(db.Model):
    __tablename__ = 'tests'
    
    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey('companies.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.SmallInteger)
    instructions = db.Column(db.Text)
    category = db.Column(db.String(255))
    num_of_questions = db.Column(db.SmallInteger, nullable=False)
    total_marks = db.Column(db.SmallInteger, nullable=False)
    active = db.Column(db.Boolean, default=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow) # Test the datetime formate.
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) # Test the datetime formate.

    # Relationships
    questions = db.relationship('Question', backref='test', cascade="all, delete-orphan")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Question(db.Model):
    __tablename__ = 'questions'
    
    id = db.Column(db.BigInteger, primary_key=True)
    test_id = db.Column(db.BigInteger, db.ForeignKey('tests.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(5), nullable=False)
    marks = db.Column(db.SmallInteger, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow) # Test the datetime formate.
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) # Test the datetime formate.

    # Relationships
    options = db.relationship('Option', backref='question', cascade="all, delete-orphan")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Option(db.Model):
    __tablename__ = 'options'
    
    id = db.Column(db.BigInteger, primary_key=True)
    question_id = db.Column(db.BigInteger, db.ForeignKey('questions.id'), nullable=False)
    test_id = db.Column(db.BigInteger, db.ForeignKey('tests.id'), nullable=False)
    option = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow) # Test the datetime formate.
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) # Test the datetime formate.

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}