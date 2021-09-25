from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField,StringField
from wtforms.validators import Email,EqualTo,Required,ValidationError

from app.models import User

class RegistrationForm(FlaskForm):
    """This defines the user registration form behaviours

    Args:
        FlaskForm ([type]): [description]
    """

    username = StringField('Username',validators = [Required()])
    email = StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Create')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')