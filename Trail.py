
from flask import make_response , abort

from config import db
from models import Trail , Trail_Schema , Trails_Schema


def ReadAll():
    READTRAILS = Trail.query.all()
    return Trails_Schema.dump(READTRAILS), 200

"""
def Create(Trail):
    Tname = Trail.get("Name")


    TRAILS[Tname] = {
        "Name": Tname,
        "Length": Trail.get("Length"),
        "Difficulty": Trail.get("Difficulty"),
        "Type": Trail.get("Type"),
        "Location": Trail.get("Location"),
    }

    reponse = {"Name": Tname}

    return reponse , 201

def ReadOne(trailId):
    if trailId in TRAILS:
        return TRAILS[trailId] , 200
    else:
        return NULL , 404
"""