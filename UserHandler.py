from flask import make_response , abort , request

from config import db
from models import User , Users_Schema , User_Schema , Users_Schema_LimitedAuthView , User_Schema_LimitedAuthView

from AuthHandler import Userlogin

# This function will return all the users in the database
def ReadAll():
    # Get the login data from the header
    login_header = request.headers.get("LoginData")
    READUSERS= User.query.all()
    # If the login data is not provided or the login data is invalid
    if not login_header or Userlogin(login_header) == False:
        return Users_Schema_LimitedAuthView.dump(READUSERS), 200

    
    READUSERS= User.query.all()
    return Users_Schema.dump(READUSERS), 200

# This function will return the user with the given userId
def ReadOne(userId):
    # Get the user with the given userId
    ReadUser = User.query.filter(User.Userid == userId).one_or_none()
    login_header = request.headers.get("LoginData")

# If the user is found
    if ReadUser:
        # If the login data is not provided or the login data is invalid
        if not login_header or Userlogin(login_header) == False:
            return User_Schema_LimitedAuthView.dump(ReadUser) , 200

        return User_Schema.dump(ReadUser) , 200
    else:
        return "User Not Found" , 404

# This function will update the user with the given userId
def Create(NewUser):
    # Get the login data from the header
    login_header = request.headers.get("LoginData")
    
    # If the login data is not provided or the login data is invalid
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Create a New User please provide login credientials" , 401

    AlreadyExists = User.query.filter(User.username == NewUser.get("username")).one_or_none()
    
    # If the user doesn't already exists
    if AlreadyExists is None:
        # Create a new user
        NewUser = User(
            Userid=None,
            username=NewUser.get("username"),
            Email=NewUser.get("Email"),
            Password=NewUser.get("Password"),
            UserPermissionLevel=NewUser.get("UserPermissionLevel")
        )
        # Add the new user to the database
        db.session.add(NewUser)
        db.session.flush()
        print(NewUser.Userid)
        db.session.commit()
        

        return {"Userid": NewUser.Userid} , 201
    else:
        abort(406, "User already exists")

    return NULL , 500

# This function will update the user with the given userId
def Delete(userId):
    # Get the login data from the header
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Delete a User please provide login credientials" , 401

    UserToDelete = User.query.filter(User.Userid == userId).one_or_none()

    # If the user is found
    if UserToDelete:
        # Delete the user
        db.session.delete(UserToDelete)
        db.session.commit()
        return "User " + str(UserToDelete.Userid) + " Successfully delted" , 200
    else:
        abort(404, "User not found")



   