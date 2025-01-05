from flask import make_response , abort , request

from config import db
from models import User , Users_Schema , User_Schema , Users_Schema_LimitedAuthView , User_Schema_LimitedAuthView

from AuthHandler import Userlogin

def ReadAll():
    login_header = request.headers.get("LoginData")
    READUSERS= User.query.all()
    if not login_header or Userlogin(login_header) == False:
        return Users_Schema_LimitedAuthView.dump(READUSERS), 200

    READUSERS= User.query.all()
    return Users_Schema.dump(READUSERS), 200

def ReadOne(userId):
    ReadUser = User.query.filter(User.Userid == userId).one_or_none()
    login_header = request.headers.get("LoginData")

    if ReadUser:
        if not login_header or Userlogin(login_header) == False:
            return User_Schema_LimitedAuthView.dump(ReadUser) , 200

        return User_Schema.dump(ReadUser) , 200
    else:
        return "User Not Found" , 404

def Create(NewUser):
    
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Create a New User please provide login credientials" , 401

    AlreadyExists = User.query.filter(User.username == NewUser.get("username")).one_or_none()
    
    if AlreadyExists is None:
        NewUser = User(
            Userid=None,
            username=NewUser.get("username"),
            Email=NewUser.get("Email"),
            Password=NewUser.get("Password"),
            UserPermissionLevel=NewUser.get("UserPermissionLevel")
        )
        db.session.add(NewUser)
        db.session.flush()
        print(NewUser.Userid)
        db.session.commit()
        

        return {"Userid": NewUser.Userid} , 201
    else:
        abort(406, "User already exists")

    return NULL , 500


def Delete(userId):
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Delete a User please provide login credientials" , 401

    UserToDelete = User.query.filter(User.Userid == userId).one_or_none()

    if UserToDelete:
        db.session.delete(UserToDelete)
        db.session.commit()
        return "User " + str(UserToDelete.Userid) + " Successfully delted" , 200
    else:
        abort(404, "User not found")



   