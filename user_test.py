from cgi import test
from user import User
from user import Credentials
import unittest
import pyperclip


class TestClass(unittest.TestCase):
    """
    test case for the User class 
    """
    def setUp(self) :
        """
        runs before each individual test run
        """
        self.new_user =User('apondi','pentatonix')
        
    def test_init(self):
        """
        check if object has been initialized correctly
        """  
        self.assertEqual(self.new_user.username, 'apondi')  
        self.assertEqual(self.new_user.password,'pentatonix')
        
    def test_save_user(self):
        """
        test if new user instance has been saved
        """ 
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)   






if __name__ == "__main__":
    unittest.main()
        
     