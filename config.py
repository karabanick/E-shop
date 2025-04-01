import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'app/static/uploads')
    UPLOADED_PHOTOS_URL = '/static/uploads/'
    UPLOADED_PHOTOS_ALLOW = ['jpg', 'jpeg', 'png', 'gif']
    UPLOADED_PHOTOS_SIZE = 4 * 1024 * 1024 # 4MB max
