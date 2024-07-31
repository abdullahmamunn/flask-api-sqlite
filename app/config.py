import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../instance/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #python -c "import secrets; print(secrets.token_hex(16))" to create secret key

    SECRET_KEY = '1431a194b91590901a78926fb3092563'  # Replace with your own secret key
    SESSION_TYPE = 'filesystem'
