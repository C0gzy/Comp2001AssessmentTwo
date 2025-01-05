from flask import make_response , abort , request

from config import db
from models import TrailPoint , TrailPoints_Schema , TrailPoint_Schema

from AuthHandler import Userlogin

def ReadAll():
    READTRAILPOINTS = TrailPoint.query.all()
    return TrailPoints_Schema.dump(READTRAILPOINTS), 200

def ReadOne(trailPointId):
    ReadTrailPoint = TrailPoint.query.filter(TrailPoint.TrailPointid == trailPointId).one_or_none()
    if ReadTrailPoint:
        return TrailPoint_Schema.dump(ReadTrailPoint) , 200
    else:
        return NULL , 404

def Create(NewTrailPoint):
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Create a TrailPoint please provide login credientials" , 401

    AlreadyExists = TrailPoint.query.filter(TrailPoint.TrailPointid == NewTrailPoint.get("TrailPointid")).one_or_none()
    
    if AlreadyExists is None:
        NewTrailPoint = TrailPoint(
            TrailPointid=NewTrailPoint.get("TrailPointid"),
            TrailPointLatitude=NewTrailPoint.get("TrailPointLatitude"),
            TrailPointLongitude=NewTrailPoint.get("TrailPointLongitude"),
            NextTrailPointid=NewTrailPoint.get("NextTrailPointid")
        )
        db.session.add(NewTrailPoint)
        db.session.flush()
        print(NewTrailPoint.TrailPointid)
        db.session.commit()
        

        return {"TrailPointid": NewTrailPoint.TrailPointid} , 201
    else:
        abort(406, "TrailPoint already exists")

    return NULL , 500

def Delete(trailPointId):
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Delete a TrailPoint please provide login credientials" , 401

    ReadTrailPoint = TrailPoint.query.filter(TrailPoint.TrailPointid == trailPointId).one_or_none()
    if ReadTrailPoint:
        db.session.delete(ReadTrailPoint)
        db.session.commit()
        return make_response(f"TrailPoint with id {trailPointId} has been deleted", 200)
    else:
        return NULL , 404

def Update(trailPointId, UpdateTrailPoint):
    login_header = request.headers.get("LoginData")
    
    if not login_header or Userlogin(login_header) == False:
        return "You're Not Authrised to Update a TrailPoint please provide login credientials" , 401

    ReadTrailPoint = TrailPoint.query.filter(TrailPoint.TrailPointid == trailPointId).one_or_none()
    if ReadTrailPoint:
        ReadTrailPoint.TrailPointLatitude = UpdateTrailPoint.get("TrailPointLatitude")
        ReadTrailPoint.TrailPointLongitude = UpdateTrailPoint.get("TrailPointLongitude")
        ReadTrailPoint.NextTrailPointid = UpdateTrailPoint.get("NextTrailPointid")
        db.session.commit()
        return TrailPoint_Schema.dump(ReadTrailPoint) , 200
    else:
        return NULL , 404