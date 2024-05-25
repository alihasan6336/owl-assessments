from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from falsk_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from application import routes
