from flask import render_template

from . import auth
from app.models import User
from .forms import RegistrationForm

@auth.route('/register')
def register():
    """This defines content of the registration page
    """
    form = RegistrationForm()


    return render_template('auth/register.html',form = form)