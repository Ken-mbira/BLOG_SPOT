from . import db

class User(db.Model):
    """This defines all behaviours of a user

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password_secure = db.Column(db.String(100))