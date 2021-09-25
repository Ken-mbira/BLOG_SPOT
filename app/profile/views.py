from flask_login.utils import login_required
from flask import render_template

from . import profile

@profile.route('/<username>')
@login_required
def profile(username):
    """This defines the contents of the profile page

    Args:
        username ([type]): [description]
    """
    return render_template('profile/profile.html')