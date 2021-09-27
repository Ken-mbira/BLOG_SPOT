from .test_create import TestApplication

from app.models import Blog, Category, Comment, Subscriber, User
from app import db

class TestUser(TestApplication):
    """This will check the behaviours of the user class

    Args:
        TestApplication ([type]): [description]
    """
    def setUp(self):
        TestApplication.setUp(self)

    def tearDown(self) -> None:
        with self.test_app.app_context():
            TestApplication.tearDown(self)

    def test_save_user(self):
        """This will check if a user is saved in the database after creation
        """
        with self.test_app.app_context():
            user = User(username = 'Ken Mbira',email = 'mbiraken17@gmail.com',)
            db.session.add(user)
            db.session.commit()

            user_found = User.query.filter_by(username = 'Ken Mbira').first()
            self.assertEqual(user.username,user_found.username)



