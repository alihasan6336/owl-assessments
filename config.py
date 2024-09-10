import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    # OAUTH_CLIENT_ID = os.environ.get('OAUTH_CLIENT_ID')
    # OAUTH_CLIENT_SECRET = os.environ.get('OAUTH_CLIENT_SECRET')
    # OAUTH_AUTHORIZE_URL = os.environ.get('OAUTH_AUTHORIZE_URL')
    # OAUTH_TOKEN_URL = os.environ.get('OAUTH_TOKEN_URL')
    # OAUTH_USERINFO_URL = os.environ.get('OAUTH_USERINFO_URL')