
from config import db ,ma
from marshmallow_sqlalchemy import fields

class Trail(db.Model):
    __tablename__ = "TRAILS"

    Trailid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TrailName = db.Column(db.String(128))
    TrailOwnerId = db.Column(db.Integer, db.ForeignKey("USERS.Userid"))
    TrailElevationgain = db.Column(db.Integer)
    TrailImageFileLocation = db.Column(db.String(512))
    TrailLength = db.Column(db.Float)
    TrailRouteType = db.Column(db.String(64))
    TrailDescription = db.Column(db.String(512))
    TrailStartingPointid = db.Column(db.Integer)

class User(db.Model):
    __tablename__ = "USERS"

    Userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    Email = db.Column(db.String(128))
    Password = db.Column(db.String(32))
    UserPermissionLevel = db.Column(db.Integer)


class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        include_relationships = True
        

Trail_Schema = TrailSchema()
Trails_Schema = TrailSchema(many=True)