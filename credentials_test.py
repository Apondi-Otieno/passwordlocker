from cgi import test
from user import User
from user import Credentials
import unittest
import pyperclip


class TestCredentials(unittest.TestCase):
    '''
    credentential model class test
    ''' 
    
    def setUp(self):
        '''
        this Method runs before each credential case
        ''' 
        self.new_credentials =Credentials('instagram','apondi','pentatonix')  
        
    def test_init(self):
        """
         check if new credentials are initialized correctly
        """ 
        self.assertEqual(self.new_credentials.account,'instagram') 
        self.assertEqual(self.new_credentials.userName,'apondi') 
        self.assertEqual(self.new_credentials.password,'pentatonix') 
        
    def save_credential_test(self):
        """
        check if credentials are saved
        """ 
        self.new_credentials.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        """
        method that cleans up after test cases have run
        """
        Credentials.credentials_list =[]
        
    def test_many_accounts(self):
        """
        saving multiple account credentials
        """   
        self.new_credentials.save_details()
        test_credential =Credentials("facebook","apondi",'pentatonix') 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_credential(self):
        """
        tests whether we can delete credentials
        """ 
        self.new_credentials.save_details()
        test_credential =Credentials("facebook","apondi",'pentatonix')
        test_credential.save_details()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_find_credentials(self):
        """
        checks if we can find a credential by account name and display details
        """ 
        self.new_credentials.save_details()
        test_credential =Credentials("facebook","apondi","pentatonix")
        test_credential.save_details()
        
        found_credential =Credentials.find_credentialls("facebook")  
        self.assertEqual(found_credential.account,test_credential.account)  
        
    def test_credential_exist(self):
        """
        tests if credentials exists
        """ 
        self.new_credentials.save_details()
        test_credential =Credentials("facebook","apondi",'pentatonix')
        test_credential.save_details()
        credentials_found =Credentials.if_credential_exist("facebook")
        self.assertTrue(credentials_found) 
        
    def test_display_credentials(self):
        """
        displays credentials
        """  
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)  
     
    def test_copy_password(self):    
       ''' 
       test to display copied password
       '''
       
       
     

if __name__ == "__main__":
    unittest.main()





