from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField
from wtforms.validators import Required

class UpdateProfileForm(FlaskForm):
    """This defines the properties of the profile form

    Args:
        FlaskForm ([type]): [description]
    """
    bio = TextAreaField('Tell us a bit about yourself',validators=[Required()])
    mobile = StringField('Enter your mobile number...',validators=[Required()])
    submit = SubmitField('Submit')