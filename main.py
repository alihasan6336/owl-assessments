import logging
logging.basicConfig(level=logging.DEBUG)
from application import app, db

try:
    with app.app_context():
        db.create_all()
except Exception as e:
    logging.exception("Failed to create tables") 