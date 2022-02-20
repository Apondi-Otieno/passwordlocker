from user import User
from user import Credentials

def new_user(username, password):
    new_user = User(username, password)
    return new_user

def save_user(user):
    user.save_user()

def display_user(user):  
    return User.display_user()

def login_user(username, password):
    check_user=Credentials.verify_user(username,password)
    return check_user

def create_user(account, username, password):
    new_user = Credentials(account, username, password)     
    return new_user

def save_user(user):
    user.save_details()
    
        
