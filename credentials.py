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

def display_user():
    return Credentials.display_user()

def delete_user(user):
    user.delete_user()

def find_user(account):
    return Credentials.find_user(account) 

def user_exists(account):
    return Credentials.if_user_exists(account)

def generate_password():
    return Credentials.copy_password(account)

def passwordlocker();
    print("welcome to password locker. \n To proceed, choose \n Acc --Create account Log -- To log in") 
    short_code=input("").lower().strip()
    if short_code=="Acc":
        print("Sign up")
        print('@' *30)
        username=input("Enter your username: ")
        while True:
            print("yp -Enter your password: \n cp- for automated password")
            password=input().lower().strip()
            if password=='yp:'   
               password== input("Enter your password \n")    
               break
            elif password=='cp:'
                password== generate_password()
                break
            else:
                print("Please enter valid password")   

        save_user(new_user(username, password))
        print("*"*30) 
        print(f"Hello {username}, Your account has been successfully created")
        print("*"*30)                  

    elif short_code== 'cp'
         print("*"*50)
         print("Enter your username and password: ")
         print("*"*50)
         username=input("username: ")
         password=input("password: ")
         login=login_user(username, password)
         if login_user==login:
             print(f"hello {username}. welcome to passlocker \n")

         while True:
             print("Use these codes: \n ca-- create account \n du--display user \n fu-- find user \n cpw--copy password \n du--delete user \n e--exit \n ")

             