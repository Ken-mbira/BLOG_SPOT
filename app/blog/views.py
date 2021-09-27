from flask_login.utils import login_required
from flask_login import current_user
from flask import redirect,url_for,flash,render_template

from app.models import Blog,Category,Comment
from . import blog
from .forms import BlogForm, CommentForm
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
    blogs = Blog.query.order_by(Blog.posted.desc()).limit(4)

    return render_template('blog/blogs.html',blogs = blogs)

@blog.route('/<title>',methods=['POST','GET'])
def show_blog(title):
    """This will render a single blog
    """
    form = CommentForm()
    blog = Blog.query.filter_by(title = title).first()
    comments = blog.comment

    if form.validate_on_submit():
        comment = Comment(comment_body = form.comment.data,author_id = current_user.id,blog_id = blog.id)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('blog.show_blog',title = title))

    return render_template('blog/blog.html',blog = blog,form = form,comments = comments)

@blog.route('/<id>/<title>')
@login_required
def delete_comment(id,title):
    """This deletes the comment
    """
    comment = Comment.query.filter_by(id = id).first()
    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('blog.show_blog',title = title))

@blog.route('/blogs/delete/<title>')
@login_required
def delete_blog(title):
    """This deletes a blog
    """
    blog = Blog.query.filter_by(title = title).first()

    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('blog.show_blogs'))

@blog.route('/<title>/update_blog',methods = ['POST','GET'])
@login_required
def update_blog(title):
    """This defines the creation of a new form
    """
    blog = Blog.query.filter_by(title = title).first()
    form = BlogForm()

    if form.validate_on_submit():
        blog.title = form.title.data
        blog.meta_title = form.title.data
        blog.body = form.blog.data
        blog.author_id = current_user.id
        db.session.add(blog)
        category = Category.query.filter_by(category_name = form.category.data).first()
        category.category.append(blog)

        db.session.commit()

        flash("Blog Updated")
        return redirect(url_for('blog.show_blogs'))

    return render_template('blog/update_blog.html',form = form)