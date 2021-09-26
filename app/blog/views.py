from flask_login.utils import login_required
from flask_login import current_user
from flask import redirect,url_for,flash,render_template

from app.models import Blog,Category,category_choice
from . import blog
from .forms import BlogForm
from app import db

@blog.route('/create_blog',methods = ['POST','GET'])
@login_required
def create_blog():
    """This defines the creation of a new form
    """
    form = BlogForm()

    if form.validate_on_submit():
        blog = Blog(title = form.title.data,meta_title = form.title.data,body = form.blog.data,author_id = current_user.id)
        db.session.add(blog)
        category = Category.query.filter_by(category_name = form.category.data).first()
        category.category.append(blog)

        db.session.commit()

        flash("Blog Created")
        return redirect(url_for('blog.show_blogs'))

    return render_template('blog/create_blog.html',form = form)

@blog.route('/blogs')
def show_blogs():
    return render_template('blog/blogs.html')
