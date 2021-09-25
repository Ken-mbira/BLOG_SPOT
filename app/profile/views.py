from flask_login.utils import login_required
from flask import render_template,request,redirect,url_for

from . import profile
from app.models import User
from app import photos,db

@profile.route('/<username>')
@login_required
def profile_index(username):
    """This defines the contents of the profile page

    Args:
        username ([type]): [description]
    """
    user = User.query.filter_by(username = username).first()
    return render_template('profile/profile.html',user = user)

@profile.route('/<username>/update_pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('profile.profile_index',username = username))