from .test_create import TestApplication

from app.models import Blog, Category, Comment, Subscriber, User
from app import db

class TestBlog(TestApplication):
    """This will check the behaviours of the user class

    Args:
        TestApplication ([type]): [description]
    """
    def setUp(self):
        TestApplication.setUp(self)
        with self.test_app.app_context():
            self.user = User(username = 'Ken Mbira',email = 'mbiraken17@gmail.com')
            self.blog = Blog(title = 'Talking to animals',author_id = self.user.id,)

    def test_instance(self):
        """This will check whether a created blog is and instance of the Blog class
        """
        self.assertTrue(isinstance(self.blog,Blog))

    def test_save_blog(self):
        """This will check if a blog can be saved to the database
        """
        with self.test_app.app_context():
            db.session.add(self.blog)
            db.session.commit()

            blog_found = Blog.query.filter_by(title = self.blog.title).first()

            self.assertEqual(self.blog.title,blog_found.title)

    def test_backref(self):
        """This will check if one can access a user using the blog
        """
        with self.test_app.app_context():
            db.session.add(self.blog)
            db.session.commit()

            blog_found = Blog.query.filter_by(title = self.blog.title).first()

            self.assertEqual(blog_found.author_id, self.user.id)     

    def tearDown(self) -> None:
        TestApplication.tearDown(self)