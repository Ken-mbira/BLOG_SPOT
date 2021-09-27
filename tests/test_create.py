import unittest
from app.models import User
from app import db
from app.models import Blog, Category, Comment, Subscriber, User

class TestApplication(unittest.TestCase):
    """This will intitalise the app

    Args:
        unittest ([type]): [description]
    """

    def setUp(self):
        """This will run before all the other tests do
        """
        from app import create_app

        self.test_app = create_app('test') 
        self.test_app.app_context().push

    def tearDown(self) -> None:
        with self.test_app.app_context():
            db.session.query(User).delete()

            db.session.query(Category).delete()

            db.session.query(Blog).delete()

            db.session.query(Comment).delete()

            db.session.query(Subscriber).delete()
            db.session.commit()
