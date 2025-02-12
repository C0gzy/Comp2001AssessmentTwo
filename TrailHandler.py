
from flask import make_response , abort , request

from config import db
from models import Trail , Trails_Schema , Trail_Schema , Trails_Schema_LimitedAuthView , Trail_Schema_LimitedAuthView
from AuthHandler import Userlogin

# This function will return all the Trails in the database
def ReadAll():
    login_header = request.headers.get("LoginData")
    READTRAILS = Trail.query.all()
    # If the login data is not provided or the login data is invalid
    if not login_header or Userlogin(login_header) == False:
        return Trails_Schema_LimitedAuthView.dump(READTRAILS), 200
    
    return Trails_Schema.dump(READTRAILS), 200

# This function will return the Trail with the given trailId
def ReadOne(trailId):
    login_header = request.headers.get("LoginData")
    ReadTrail = Trail.query.filter(Trail.Trailid == trailId).one_or_none()
    if ReadTrail:
        if not login_header or Userlogin(login_header) == False:
            return Trail_Schema_LimitedAuthView.dump(ReadTrail) , 200

        return Trail_Schema.dump(ReadTrail) , 200
    else:
        return {"response" : "Trail not found or doesn't exist"} , 404

# This function will create a new Trail
def Create(NewTrail):

    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Create a New Trail please provide login credientials" , 401

    AlreadyExists = Trail.query.filter(Trail.TrailName == NewTrail.get("TrailName")).one_or_none()
    
    if AlreadyExists is None:
        # Create a new Trail
        NewTrail = Trail(
            Trailid=None,
            TrailName=NewTrail.get("TrailName"),
            TrailOwnerId=NewTrail.get("TrailOwnerId"),
            TrailElevationgain=NewTrail.get("TrailElevationgain"),
            TrailImageFileLocation=NewTrail.get("TrailImageFileLocation"),
            TrailLength=NewTrail.get("TrailLength"),
            TrailRouteType=NewTrail.get("TrailRouteType"),
            TrailDescription=NewTrail.get("TrailDescription"),
            TrailStartingPointid=NewTrail.get("TrailStartingPointid")
        )
        db.session.add(NewTrail)
        db.session.flush()
        print(NewTrail.Trailid)
        db.session.commit()
        

        return {"Trailid": NewTrail.Trailid} , 201
    else:
        abort(406, "Trail already exists")

    return {"response" : "Internal Server Error"} , 500

# This function will update the Trail with the given trailId
def Update(trailId,UpdatedTrail):
    login_header = request.headers.get("LoginData")
    
    # If the login data is not provided or the login data is invalid
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Update a Trail please provide login credientials" , 401

    TrailToUpdate = Trail.query.filter(Trail.Trailid == trailId).one_or_none()

    if TrailToUpdate:
        # Update the Trail
        TrailToUpdate.TrailName = UpdatedTrail.get("TrailName")
        TrailToUpdate.TrailOwnerId = TrailToUpdate.TrailOwnerId
        TrailToUpdate.TrailElevationgain = UpdatedTrail.get("TrailElevationgain")
        TrailToUpdate.TrailImageFileLocation = UpdatedTrail.get("TrailImageFileLocation")
        TrailToUpdate.TrailLength = UpdatedTrail.get("TrailLength")
        TrailToUpdate.TrailRouteType = UpdatedTrail.get("TrailRouteType")
        TrailToUpdate.TrailDescription = UpdatedTrail.get("TrailDescription")
        TrailToUpdate.TrailStartingPointid = UpdatedTrail.get("TrailStartingPointid")
        db.session.commit()
        return "Trail "+ str(trailId) +" Successfully Updated" , 200
    else:
        abort(404, "Trail not found")


# This function will delete the Trail with the given trailId
def Delete(trailId):
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Delete a Trail please provide login credientials" , 401

    TrailToDelete = Trail.query.filter(Trail.Trailid == trailId).one_or_none()

    if TrailToDelete:
        db.session.delete(TrailToDelete)
        db.session.commit()
        return "Trail "+ str(TrailToDelete.Trailid) +" Successfully delted" , 200
    else:
        abort(404, "Trail not found")