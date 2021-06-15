import os

SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(**{
  'user': 'admin',
  'password': 'admin',
  'host': 'spidy-backend_db_1',
  'port': '5432',
  'db_name': 'spidy.db'
})
SECRET_KEY = os.urandom(24)

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_NATIVE_UNICODE = 'utf-8'