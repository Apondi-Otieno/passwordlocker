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