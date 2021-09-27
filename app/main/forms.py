from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class SubscriptionForm(FlaskForm):
    """This form defines all data needed to create a subscription

    Args:
        FlaskForm ([type]): [description]
    """
    email = StringField('Enter the email you wish to receive alerts on',validators=[Required()])
    name = StringField('Enter your name:',validators=[Required()])
    submit = SubmitField('Submit')