#BDD
# 
! Create a username and password
! Record The name of the user
! save the username and password
! create new account inpt new username and password
! generate new password or create a new one
! view accounts and respective passwords
! delete accounts no longer in use
# 
# 

import random
import pyperclip
import string

# user class

class user:

    user_list = []

    def __init__(self, username,password):
        self.username = username
        self.password = password

# this will save new user details

    def save_user(self):

      user.user_list.append(self)

      @classmethod

#this will display user details

      def display_user(cls):
          return cls.user_list

#this will delete user details

      def delete_user(self):

    user.user_list.remove(self)


# new class

class Credentials():

    credentials_list = []

    @classmethod
    def verify_user(cls,username,password):

        a_user =""
for user in User.user_list:
    if(user,username==username and user.password==password):
        a_user==user.username
        return a_user


# storing user details

        def __init__(self,account,username,password):

            self.account = account
            self.username = username
            self.password = password

        def save_details(self):

            Credentials.credentials_list.append(self)

        def delete_credentials(self):

            Credentials.credentials_list.remove(self)


   @classmethod

 # this method takes in account name and returns a matching password

 def find_credentials(cls,account):
     for Credentials in cls.credentials_list:
         if credential.account == account:
             return credential

    @classmethod

#this method will let the user copy the passwords from

def copy_password(cls,account):
    found_credentials =Credentials.find_credentials(account)
    pyperclip.copy(found_credentials.password)
    password_copied=pyperclip.paste()
    print (password_copied)
