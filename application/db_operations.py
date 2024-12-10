from application import db
from application.models import Company

def insert_in_db(record):
    db.session.add(record)
    db.session.commit()

def get_all_companies():
    return Company.query.all()