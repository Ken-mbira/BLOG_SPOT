from flask_login import UserMixin

from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

from . import db


class Category(db.Model):
    """This defines all the topics that a blog may be about

    Args:
        db ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key = True)
    category_name = db.Column(db.String)

category_choice = db.Table('category_choice',
    db.Column('blog_id',db.Integer,db.ForeignKey('blogs.id')),
    db.Column('category_id',db.Integer,db.ForeignKey('category.id'))
)

class Blog(db.Model):
    """Defines all behaviours of a blog

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    meta_title = db.Column(db.String(200))
    body = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category = db.relationship('Category',secondary=category_choice,backref=db.backref('category',lazy = 'dynamic'))
    comment = db.relationship('Comment', backref='blog', lazy="dynamic")

    def __repr__(self):
        return self.title

class User(UserMixin,db.Model):
    """This defines all behaviours of a user

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True,index=True)
    bio = db.Column(db.String(200))
    mobile = db.Column(db.String(200))
    profile_pic_path = db.Column(db.String(200))
    password_secure = db.Column(db.String(200))
    blogs = db.relationship('Blog', backref='author')
    comment = db.relationship('Comment', backref='author', lazy="dynamic")

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

class Comment(db.Model):
    """This will define all properties of a comment

    Args:
        db ([type]): [description]
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True)
    comment_body = db.Column(db.String(255))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))