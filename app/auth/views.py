from flask import render_template,flash,redirect,url_for
from flask_login import login_user
from flask_login.utils import login_required,logout_user

from app import db,login_manager
from . import auth
from app.models import User
from .forms import RegistrationForm,LoginForm

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

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

@auth.route('/login',methods=["GET","POST"])
def login():
    """This renders the content of the login page
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))

        flash("Either the email or password input is wrong, please check them again")

    return render_template('auth/login.html',form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))