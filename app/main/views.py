from flask import render_template,redirect,url_for
from flask_login.utils import login_required

from . import main
from app.request import get_quotes, process_quote
from app.models import Subscriber, Category
from .forms import SubscriptionForm,CategoryForm
from app import db

@main.route('/')
def index():
    quotes = process_quote(get_quotes())
    return render_template('index.html',quote = quotes)

@main.route('/subscribe',methods=['GET','POST'])
def subscribe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        sub = Subscriber(email = form.email.data,name = form.name.data)
        db.session.add(sub)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('subscribe.html',form = form)

@main.route('/category',methods=['GET','POST'])
@login_required
def category():
    """This will render the template to show
    """
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(category_name = form.name.data)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('category.html',form = form)
