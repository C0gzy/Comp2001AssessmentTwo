
from flask import make_response , abort

from config import db
from models import Trail , Trails_Schema , Trail_Schema 


def ReadAll():
    READTRAILS = Trail.query.all()
    return Trails_Schema.dump(READTRAILS), 200


def Create(NewTrail):

    AlreadyExists = Trail.query.filter(Trail.TrailName == NewTrail.get("TrailName")).one_or_none()

    if AlreadyExists is None:
        NewTrail = Trail_Schema.load(NewTrail, session=db.session)
        db.session.add(NewTrail)
        db.session.flush()
        db.session.commit()
        return NewTrail.TrailId , 201
    else:
        abort(406, "Trail already exists")

    return NULL , 500


    

"""
def ReadOne(trailId):
    if trailId in TRAILS:
        return TRAILS[trailId] , 200
    else:
        return NULL , 404
"""