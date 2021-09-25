from flask import render_template

from . import auth

@auth.route('/register')
def register():
    """This defines content of the registration page
    """
    return render_template('auth/register.html')