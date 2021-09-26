from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField,RadioField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    """This defines all the data to be collected from a user for the blog

    Args:
        FlaskForm ([type]): [description]
    """

    title = StringField('Enter the title of the blog',validators=[Required()])
    meta_title = StringField('Enter a brief summary of the blog',validators=[Required()])
    blog = TextAreaField('Enter the blog itself')
    category = RadioField('Enter the category in which your blog falls',validators=[Required()],choices=[('technology'),('finance'),('religion'),('fashion'),('food'),('music'),('lifestyle'),('sports'),('travel'),('politics'),('movie'),('gaming'),('cars')])
    submit = SubmitField('Create Blog')

class CommentForm(FlaskForm):
    """This defines the data to be collected from the comment form

    Args:
        FlaskForm ([type]): [description]
    """
    comment = StringField('Enter your comment below',validators=[Required()])
    submit = SubmitField('Submit')