import os

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(**{
  'user': 'postgres',
  'password': 'postgres',
  'host': 'spidy-db',
  'port': '5432',
  'db_name': 'db'
})
SECRET_KEY = os.urandom(24)

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_NATIVE_UNICODE = 'utf-8'