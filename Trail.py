
TRAILS = {
    "Trail1": {
        "Name": "Trail1",
        "Length": 5,
        "Difficulty": "Easy",
        "Type": "Loop",
        "Location": "Park1",
    }
}


def ReadAll():
    return list(TRAILS.values())

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