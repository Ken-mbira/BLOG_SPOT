from flask import render_template

from . import main
from app.request import get_quotes, process_quote
from app.models import Subscriber, User
from .forms import SubscriptionForm
from app import db

@main.route('/')
def index():
    quotes = process_quote(get_quotes())
    return render_template('index.html',quote = quotes)

@main.route('/subscribe')
def subscribe():
    form = SubscriptionForm()
    if form.validate_on_submit():
        sub = Subscriber(email = form.email.data,name = form.name.data)
        db.session.add(sub)
        db.session.commit()
    return render_template('subscribe.html',form = form)