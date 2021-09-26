from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField

class UpdateProfileForm(FlaskForm):
    """This defines the properties of the profile form

    Args:
        FlaskForm ([type]): [description]
    """
    bio = TextAreaField('Tell us a bit about yourself')
    mobile = StringField('Enter your mobile number...')
    submit = SubmitField('Submit')