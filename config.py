import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "wow-thats-test-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATEBASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
