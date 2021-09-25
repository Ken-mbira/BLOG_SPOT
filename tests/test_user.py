import unittest

from app.models import User

class TestUser(unittest.TestCase):
    """This will check all the behaviours of the user class

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """This runs before every test does
        """
        self.user = User(username = 'Ken Mbira',email = 'mbiraken17@gmail.com',password = "mandizi")

    def test_instance(self):
        """This will check whether the user class instance is being instantiated correctly
        """
        self.assertTrue(isinstance(self.user,User))

    def test_password_verification(self):
        """This checks whether the password verification is taking place correctly
        """
        password = 'mandizi'
        self.assertTrue(self.user.verify_password(password),"The password verifyer is not working")

    def test_no_access_password(self):
        """This will check that the password cannot be accessed
        """
        with self.assertRaises(AttributeError):
            self.user.password