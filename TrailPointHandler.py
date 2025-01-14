from flask import make_response , abort , request

from config import db
from models import TrailPoint , TrailPoints_Schema , TrailPoint_Schema

from AuthHandler import Userlogin

# This function will return all the TrailPoints in the database
def ReadAll():
    # Get the login data from the header
    READTRAILPOINTS = TrailPoint.query.all()
    return TrailPoints_Schema.dump(READTRAILPOINTS), 200

def ReadOne(trailPointId):
    ReadTrailPoint = TrailPoint.query.filter(TrailPoint.TrailPointid == trailPointId).one_or_none()
    if ReadTrailPoint:
        return TrailPoint_Schema.dump(ReadTrailPoint) , 200
    else:
        return {"response" : "TrailPoint Not Found"} , 404

# This function will create a new TrailPoint
def Create(NewTrailPoint):
    login_header = request.headers.get("LoginData")
    
    # If the login data is not provided or the login data is invalid
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Create a TrailPoint please provide login credientials" , 401

    AlreadyExists = TrailPoint.query.filter(TrailPoint.TrailPointid == NewTrailPoint.get("TrailPointid")).one_or_none()
    
    if AlreadyExists is None:
        # Create a new TrailPoint
        NewTrailPoint = TrailPoint(
            TrailPointid=NewTrailPoint.get("TrailPointid"),
            TrailPointLatitude=NewTrailPoint.get("TrailPointLatitude"),
            TrailPointLongitude=NewTrailPoint.get("TrailPointLongitude"),
            NextTrailPointid=NewTrailPoint.get("NextTrailPointid")
        )
        db.session.add(NewTrailPoint)
        db.session.commit()
        

        return {"TrailPointid": NewTrailPoint.TrailPointid} , 201
    else:
        abort(406, "TrailPoint already exists")

    return {"Response" : "Internal Server Error"} , 500

# This function will delete the TrailPoint with the given TrailPointId
def Delete(trailPointId):
    login_header = request.headers.get("LoginData")
    
    # If the login data is not provided or the login data is invalid
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Delete a TrailPoint please provide login credientials" , 401

    ReadTrailPoint = TrailPoint.query.filter(TrailPoint.TrailPointid == trailPointId).one_or_none()
    if ReadTrailPoint:
        db.session.delete(ReadTrailPoint)
        db.session.commit()
        return make_response(f"TrailPoint with id {trailPointId} has been deleted", 200)
    else:
        return {"response" : "Trail not found"} , 404

# This function will update the TrailPoint with the given TrailPointId
def Update(trailPointId, UpdateTrailPoint):
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Update a TrailPoint please provide login credientials" , 401

    
    ReadTrailPoint = TrailPoint.query.filter(TrailPoint.TrailPointid == trailPointId).one_or_none()
    if ReadTrailPoint:
        # Update the TrailPoint
        ReadTrailPoint.TrailPointLatitude = UpdateTrailPoint.get("TrailPointLatitude")
        ReadTrailPoint.TrailPointLongitude = UpdateTrailPoint.get("TrailPointLongitude")
        ReadTrailPoint.NextTrailPointid = UpdateTrailPoint.get("NextTrailPointid")
        db.session.commit()
        return TrailPoint_Schema.dump(ReadTrailPoint) , 200
    else:
        return {"response" : "Trail not found"} , 404