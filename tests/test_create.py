import unittest
from app.models import User
from app import db

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
