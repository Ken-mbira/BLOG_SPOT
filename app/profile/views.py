from flask_login.utils import login_required
from flask import render_template,request,redirect,url_for,abort

from . import profile
from app.models import User
from app import photos,db
from .forms import UpdateProfileForm

@profile.route('/<username>',methods=["GET","POST"])
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
    """This is responsible for updating the user profile pic

    Args:
        username ([type]): [description]

    Returns:
        [type]: [description]
    """
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('profile.profile_index',username = username))

@profile.route('/<username>/update_profile',methods = ["POST","GET"])
@login_required
def update_profile(username):
    """This is responsible for updating the user profile

    Args:
        username ([type]): [description]
    """
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)
    else:
    

        form = UpdateProfileForm()

        if form.validate_on_submit():
            user.bio = form.bio.data
            user.mobile = form.mobile.data

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('profile.profile_index',username = user.username))

        return render_template('profile/update_profile.html',form = form)