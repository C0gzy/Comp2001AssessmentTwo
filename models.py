
from config import db ,ma


class Trail(db.Model):
    __tablename__ = "TRAILS"

    Trailid = db.Column(db.Integer, primary_key=True)
    TrailName = db.Column(db.String(128))
    TrailOwnerId = db.Column(db.Integer)
    TrailElevationgain = db.Column(db.Integer)
    TrailImageFileLocation = db.Column(db.String(512))
    TrailLength = db.Column(db.Float)
    TrailRouteType = db.Column(db.String(64))
    TrailDescription = db.Column(db.String(512))
    TrailStartingPointid = db.Column(db.Integer)




class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        

Trail_Schema = TrailSchema()
Trails_Schema = TrailSchema(many=True)