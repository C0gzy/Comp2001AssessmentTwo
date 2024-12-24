
from flask import make_response , abort

from config import db
from models import Trail , Trails_Schema , Trail_Schema 


def ReadAll():
    READTRAILS = Trail.query.all()
    return Trails_Schema.dump(READTRAILS), 200

def ReadOne(trailId):
    ReadTrail = Trail.query.filter(Trail.Trailid == trailId).one_or_none()
    if ReadTrail:
        return Trail_Schema.dump(ReadTrail) , 200
    else:
        return NULL , 404

def Create(NewTrail):

    AlreadyExists = Trail.query.filter(Trail.TrailName == NewTrail.get("TrailName")).one_or_none()

    if AlreadyExists is None:
        NewTrail = Trail_Schema.load(NewTrail, session=db.session)
        db.session.add(NewTrail)
        db.session.flush()
        db.session.commit()
        return NewTrail.Trailid , 201
    else:
        abort(406, "Trail already exists")

    return NULL , 500

def Delete(trailId):
    TrailToDelete = Trail.query.filter(Trail.TrailId == trailId).one_or_none()

    if TrailToDelete:
        db.session.delete(TrailToDelete)
        db.session.commit()
        return "Trail "+TrailToDelete.Trailid+" Successfully delted" , 200
    else:
        abort(404, "Trail not found")