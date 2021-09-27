from flask import render_template

from . import main
from app.request import get_quotes, process_quote
from app.models import User

@main.route('/')
def index():
    quotes = process_quote(get_quotes())
    return render_template('index.html',quote = quotes)