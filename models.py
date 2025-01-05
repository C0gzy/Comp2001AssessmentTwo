
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

    trails = db.relationship(
        Trail, 
        backref="USERS", 
        
        )

class TrailPoint(db.Model):
    __tablename__ = "TRAILPOINT"
    TrailPointid = db.Column(db.Integer, primary_key=True)
    TrailPointLatitude = db.Column(db.Float)
    TrailPointLongitude = db.Column(db.Float)
    NextTrailPointid = db.Column(db.Integer, db.ForeignKey("TRAILPOINT.TrailPointid"))


class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        include_relationships = True
        include_fk = True
        
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_relationships = True

class TrailPointSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrailPoint
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True

Trail_Schema = TrailSchema()
Trail_Schema_LimitedAuthView = TrailSchema(exclude=["TrailOwnerId","TrailImageFileLocation","USERS"])
Trails_Schema = TrailSchema(many=True)
Trails_Schema_LimitedAuthView = TrailSchema(many=True , exclude=["TrailOwnerId","TrailImageFileLocation","USERS"])


User_Schema = UserSchema()
User_Schema_LimitedAuthView = UserSchema(exclude=["Password","UserPermissionLevel","trails","Email","Userid"])
Users_Schema = UserSchema(many=True)
Users_Schema_LimitedAuthView = UserSchema(many=True , exclude=["Password","UserPermissionLevel","trails","Email"])

TrailPoint_Schema = TrailPointSchema()
TrailPoints_Schema = TrailPointSchema(many=True)
