from flask import Flask
from config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from authlib.integrations.flask_client import OAuth


load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# oauth = OAuth(app)
# oauth.register(
#     name='oauth_provider',
#     client_id=app.config['OAUTH_CLIENT_ID'],
#     client_secret=app.config['OAUTH_CLIENT_SECRET'],
#     authorize_url=app.config['OAUTH_AUTHORIZE_URL'],
#     token_url=app.config['OAUTH_TOKEN_URL'],
#     userinfo_endpoint=app.config['OAUTH_USERINFO_URL'],
#     client_kwargs={'scope': 'openid profile email'}
# )
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

from application import routes
