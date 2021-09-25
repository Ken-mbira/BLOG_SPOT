from flask import render_template

from . import auth
from app.models import User
from .forms import RegistrationForm,LoginForm

@auth.route('/register')
def register():
    """This defines content of the registration page
    """
    form = RegistrationForm()


    return render_template('auth/register.html',form = form)

@auth.route('/login')
def login():
    """This renders the content of the login page
    """
    form = LoginForm()
    return render_template('auth/login.html',form = form)