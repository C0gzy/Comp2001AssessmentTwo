from flask import make_response , abort

from config import db
from models import User , Users_Schema , User_Schema 

def ReadAll():
    READUSERS= User.query.all()
    return Users_Schema.dump(READUSERS), 200

def ReadOne(userId):
    ReadUser = User.query.filter(User.Userid == userId).one_or_none()
    if ReadUser:
        return User_Schema.dump(ReadUser) , 200
    else:
        return "User Not Found" , 404

def Create(NewUser):
    
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
    UserToDelete = User.query.filter(User.Userid == userId).one_or_none()

    if UserToDelete:
        db.session.delete(UserToDelete)
        db.session.commit()
        return "User " + str(UserToDelete.Userid) + " Successfully delted" , 200
    else:
        abort(404, "User not found")