from application import db
from application.models import Companies

def insert_in_db(record):
    db.session.add(record)
    db.session.commit()

def get_all_companies():
    return Companies.query.all()