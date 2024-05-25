import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key_123"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://postgres:postgresadmin@localhost:5432/flask_db"