from werkzeug.security import generate_password_hash,check_password_hash

from . import db

class User(db.Model):
    """This defines all behaviours of a user

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True,index=True)
    password_secure = db.Column(db.String(200))

    @property
    def password(self):
        """This will prevent reading of the password
        """
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self,password):
        """This will turn the password into hashes

        Args:
            password ([string]): [This is the input password]
        """
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        """This will check the set series of hashes and the hashes from the inputted password to see if they match

        Args:
            password ([string]): [This is the input password]
        """
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'