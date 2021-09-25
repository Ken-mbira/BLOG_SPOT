import time
from flask import render_template,flash,redirect,url_for

from app import db
from . import auth
from app.models import User
from .forms import RegistrationForm,LoginForm

@auth.route('/register',methods= ["GET","POST"])
def register():
    """This defines content of the registration page
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Your account has been successfully created.","success")
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form = form)

@auth.route('/login')
def login():
    """This renders the content of the login page
    """
    form = LoginForm()
    return render_template('auth/login.html',form = form)